##Conference Organization App. - FSD Project 4

This application uses Google Cloud API's, OAuth, and Endpoints for a Conference App. that allows a developer to create horizontally scalable applications quickly and available to a variety of platforms. In this conference app., users can edit their profile, create and register conferences, create sessions, view and sort by conferences and sessions, as well as additional functionality as mentioned in the following README file.

###The Repo. Contains the Following Files
-------------------------------------
 1. /ud858/ConferenceCentral_Complete - Project files were provided by Udacity and modified and/or expanded upon for the Lesson to implement additional functionality as explained in the Tasks below.
 2. /ud858/ConferenceCentral_Complete/settings.py - Google API Client ID's set here.
 3. /ud858/ConferenceCentral_Complete/conference.py - Endpoints and utility methods to create, edit, and view conference, session, and profiles, etc.
 4. /ud858/ConferenceCentral_Complete/models.py - Models for the app. Conference, Session, Profile classes.
 5. /ud858/ConferenceCentral_Complete/queue.py - Queue config file for tasks.
 6. README.md
 
###Requirements
--------------------
 1. The user must have a Google account.
 2. The user must create a new project in the Google Developer's Console and copy over the following: The application name must be changed in app.yaml. The CLIENT_ID must be changed in static/js/app.js. The client ID's in the settings.py file must be obtained from the API's and changed.
 3. Updating your user profile at <code>/profile</code> should be the first step after the app. has started running. It is required to associate conferences and sessions with an authenticated profile.
 4. Google App Engine SDK is required to test and deploy to the app engine production environment. [https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
 5. Testing locally can be done through the APIs Explorer: <code>http://localhost:8080/_ah/api/explorer</code>
 6. Viewing the data in the Datastore Viewer: <code>http://localhost:8001/datastore?kind=Conference</code>
 
###How to Run the Application
-------------------------
<p>Python 2.7, the endpoints module, and GoogleAppEngineLauncher must be installed and configured.</p>

<pre>
    <code>$ pip install endpoints</code>
	<code>$ git clone https://github.com/mikelewek/FSD_P4_ConferenceApp.git</code>
	<code></code>
</pre>

###Task #1 - Explanation of Design Choices

* The Session and SessionForm model and endpoints were created as necessary, utilizing required variables in the project outline.
* The Session class properties: typeOfSession and speakerKey endpoints were created. A speakerKey property was added to the Session and SessionForm class to create a ancestor relationship with a speaker's profile entity key, to allow the user to assign and sort by speaker. A typeOfSession property was added to the Session and SessionForm model which allows the user to insert and sort by type. 
* An endpoint was created to get all sessions (getConferenceSessions). The CONF_GET_REQUEST is set as the request message class and SessionForm is set as the response message class. Sessions are queried in the datastore using the websafeConferenceKey and a SessionForm message object is returned containing all sessions.
* The getConferenceSessionsByType endpoint uses CONF_GET_TYPE_REQUEST as the request message class. The websafeConferenceKey is queried and returned from the datastore, if it exists. The SessionForms form message is returned as the response message.
* The getSessionsBySpeaker endpoint uses CONF_GET_SPEAKER_REQUEST as the request message class. Sessions are queried, replicating the previous two functions.
* Wishlist endpoints were created as described in Task #2 below.
* The getConferenceSessionsByHighlights endpoint queries a conference and filters by highlights similar the the getSessionsBySpeaker and getConferenceSessionsByType endpoints above.
* The getProfileByEmail endpoint queries a user's profile by email using PROFILE_GET_EMAIL_REQUEST as teh request message class and EmailForms as the response class.

###Task #2 - Add Session to Wishlist
Wishlist endpoints were implemented as required. addSessionToWishlist(SessionKey), getSessionsInWishlist(), deleteSessionInWishlist(SessionKey)

A wishList repeated list property was added to the Profile model class and functionality was added to iterate a user's profile to get, add, or remove sessions from the wishlist if they had authorization.

###Task #3 - Indexes and additional two queries
Indexes added:

Two additional queries added: None

1. getConferenceSessionsByHighlights(websafeConferenceKey, highlights) - Retrieves conference sessions by highlight.
2. getProfileByEmail(mainEmail) - Allows conference organizer to retrieve a registered user's profile by entering their email address.