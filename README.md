##Conference Organization App. - FSD Project 4

This application uses Google Cloud API's, OAuth, and Endpoints for a Conference App. Users can edit their profile, create and register conferences, view conferences, conference details, and which conferences a user has created and attended.

###The Repo. Contains the Following Files
-------------------------------------
 1. /ud858/ConferenceCentral_Complete - Files were provided by Udacity and modified for the Lesson to implement additional functionality as explained in the Tasks below.
 2. README.md
 
 
###Requirements
--------------------
 1. The user must have a Google account.
 2. The user must create a new project in the Google Developer's Console and copy over the following: The application name must be changed in app.yaml. The CLIENT_ID must be changed in static/js/app.js.
 3. Google App Engine SDK is required to test and deploy to the app engine production environment. [https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
  
###How to Run the Application
-------------------------
<p>Python 2.7, the endpoints module, and GoogleAppEngineLauncher must be installed and configured.</p>

<pre>
    <code>$ pip install endpoints</code>
	<code>$ git clone https://github.com/mikelewek/FSD_P4_ConferenceApp.git</code>
	<code></code>
</pre>

###Task #1 - Explanation of Design Choices
The Session class, SessionForm class, and Endpoints were created, utilizing required variables in the project outline.
An Endpoint and function was created to get all sessions (getConferenceSessions). The CONF_GET_REQUEST is set as the request message class and SessionForm is set as the response message class. Sessions are queried and a SessionForm message object is returned containing all sessions. If memcache contains the key, the data is returned from cache, otherwise it queries the datastore. 
All sessions by type (getConferenceSessionsByType) uses CONF_GET_TYPE_REQUEST as the request message class. Sessions are queried and managed with memcache, mirroring the previous function.
All sessions by speaker (getSessionsBySpeaker) uses CONF_GET_SPEAKER_REQUEST as the request message class. Sessions are queried, replicating the previous two functions, if cache data is not available.
