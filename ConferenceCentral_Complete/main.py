#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import logging
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache

from conference import ConferenceApi
from models import Session

MEMCACHE_SPEAKER_KEY = "FEATURED SPEAKER"


class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )


class GetFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Set featured speaker using memcache"""
        # get sessions by websafeConferenceKey
        conference_key = ndb.Key(urlsafe=self.request.get('websafeConferenceKey'))
        query = Session.query(ancestor=conference_key)

        # loop results checking for speakerKey equal to new speakerKey
        # set dict memcache if speaker occurs in a session
        session_data = {}
        session_data['speakerKey'] = self.request.get('speakerKey')
        session_data['sessionName'] = []

        i = 0
        for row in query:
            # set featured speaker if speakerKey exists
            # add session names to list
            if row.speakerKey == self.request.get('speakerKey'):
                session_data['sessionName'].append(row.sessionName)
                i += 1

        # check if speakerKey dict was set
        if i > 1:
            memcache.set(self.request.get('websafeConferenceKey'),
                         session_data)

        self.response.set_status(204)


app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/get_featured_speaker', GetFeaturedSpeakerHandler),
], debug=True)
