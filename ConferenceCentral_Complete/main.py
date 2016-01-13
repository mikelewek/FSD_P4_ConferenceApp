#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.ext import ndb
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache

from conference import ConferenceApi
from models import Session
from models import Speaker

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


class SetFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Set featured speaker using memcache"""

        # set conference_key var to request var
        conference_key = ndb.Key(urlsafe=self.request.get('websafeConferenceKey'))

        # loop results checking for speakerKey equal to new speakerKey
        # set dict memcache if speaker occurs in a session
        session_data = {}
        session_data['sessionName'] = []

        query = Session.query(ancestor=conference_key)\
            .filter(Session.speakerKey == self.request.get('speakerKey'))
        num_sessions = query.count()

        # get speaker displayName from speaker datastore and set into dict
        display_name = ndb.Key(urlsafe=self.request.get('speakerKey')).get()
        session_data['displayName'] = display_name.displayName

        for q in query:
            if num_sessions > 1:
                session_data['sessionName'].append(q.sessionName)
                memcache.set(self.request.get('websafeConferenceKey'), session_data)

        self.response.set_status(204)


app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/set_featured_speaker', SetFeaturedSpeakerHandler),
], debug=True)
