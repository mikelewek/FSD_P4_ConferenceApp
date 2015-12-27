##Conference Organization App. - FSD Project 4

This application uses Google Cloud API's, OAuth, and Endpoints for a Conference App. Users can edit their profile, create and register conferences, view conferences, conference details, and which conferences a user has created and attended.

###The Repo. Contains the Following Files
-------------------------------------
 1. /ud858/ConferenceCentral_Complete - Proect files were provided by Udacity and modified for the Lesson to implement additional functionality as explained in the Tasks below.
 2. README.md
 
 
###Requirements
--------------------
 1. The user must have a Google account.
 2. The user must create a new project in the Google Developer's Console and copy over the following: The application name must be changed in app.yaml. The CLIENT_ID must be changed in static/js/app.js. The WEB_CLIENT_ID must be changed in settings.py.
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
* The Session class properties: typeOfSession and speakerKey were added to allow the user to sort by type and speaker.
* An endpoint was created to get all sessions (getConferenceSessions). The CONF_GET_REQUEST is set as the request message class and SessionForm is set as the response message class. Sessions are queried in the datastore using the websafeConferenceKey and a SessionForm message object is returned containing all sessions.
* The getConferenceSessionsByType method uses CONF_GET_TYPE_REQUEST as the request message class. The websafeConferenceKey is queried and returned from the datastore, if it exists. The SessionForms form message is returned as the response message.
* The getSessionsBySpeaker method uses CONF_GET_SPEAKER_REQUEST as the request message class. Sessions are queried, replicating the previous two functions.

###Task #2 - Add Session to Wishlist
Wishlist endpoints were implemented as required. addSessionToWishlist(SessionKey), getSessionsInWishlist(), deleteSessionInWishlist(SessionKey)

A wishList repeated list property was added to the Profile model class and functionality was added to iterate a user's profile to get, add, or remove sessions from the wishlist if they had authorization.

###Task #3 - Indexes and additional two queries
Indexes added:

Two additional queries added:

1. getConferenceSessionsByHighlights(websafeConferenceKey, highlights) - Retrieves conference sessions by highlight.
2. getProfileByEmail(mainEmail) - Retrieves profile by entering email address. 