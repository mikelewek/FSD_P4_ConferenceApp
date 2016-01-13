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
	
	Additional steps for setting up and running the app. in either the Google App. Engine or deploying, is provided in Udacity's readme file located: <code>/ud858/ConferenceCentral_Complete/README.md</code>
</pre>

###Task #1 - Explanation of Design Choices

#####Notes
* The Session and SessionForm model and endpoints were created as necessary, utilizing required variables in the project outline.
* The Session model was set as StringProperty for sessionName, highlights, typeOfSession, and speakerKey properties since they will be inserted and queried as text. DateProperty was used for the date field, TimeProperty for the time field, and integer properties where necessary, so they are in the correct format and will be easy to use as an API user and query. To create a Session, sessionName is set as required.
* The Session class properties: typeOfSession and speakerKey endpoints were created. A typeOfSession property was added to the Session and SessionForm model which allows the user to insert and sort by type. The speakerKey is a user's email address and inserted manully by the API user.
* An endpoint was created to get all sessions (getConferenceSessions). The CONF_GET_REQUEST is set as the request message class and SessionForm is set as the response message class. Sessions are queried in the datastore using the websafeConferenceKey and a SessionForm message object is returned containing all sessions.
* The getConferenceSessionsByType - The websafeConferenceKey is queried and returned from the datastore, if it exists. The SessionForms form message is returned as the response message.
* The getSessionsBySpeaker - Sessions are queried, replicating the previous two functions. They speakerKey StringProperty was added to the Session model.
* Wishlist endpoints were created as described in Task #2 below.
* The getConferenceSessionsByHighlights endpoint queries a conference and filters by highlights similar the the getSessionsBySpeaker and getConferenceSessionsByType endpoints above. ConferenceKeysToAttend was added as a repeated StringProperty to the Profile model, since multiple items can be stored for each user as a list. The same is true for the wishlist items.
* The getProfileByEmail endpoint queries a user's profile by email using PROFILE_GET_REQUEST as the request message class and Conferenceform as the response class. 
* The getFeaturedSpeaker endpoint gets the featured speaker profile if it exists in memcache. A speakerForm model was created to return sessionName and displayName properties.
* The SetFeaturedSpeakerHandler in main.py is used to set featured speaker tasks by setting it in memcache when a new session object is created in the _createSessionObject utility function. If there is more than one session by a speaker at a conference, a new Memcache entry that features the speaker and session names is inserted for that conference.

#####How the User Should Interact with API to Add a Session and Get The Featured Speaker for a Conference

1. A user decides that she wants to add a Session to a conference.
2. She checks out the createSession endpoint and notices that she needs to provide a speakerKey.
3. She finds the addSpeaker endpoint and inputs the information for a Speaker 'John Smith'.
4. After submitting the form to addSpeaker she receives a response from the server confirming that a new Speaker object has been created. The Key pointing to the object is a long string which serves as a unique reference. She copies that string.
5. Returning to the createSession endpoint the user copies the speakerKey string into the form in the appropriate field and fills out the rest of the form.
6. A task is then set to run, assigning the speaker in memcache if the speaker is set to speak at more than one of the sessions at a conference.
7. She can then get a conference's featured speaker by using the getFeaturedSpeaker endpoint by inserting the websafeConferenceKey string into the form. (as long as the same person is assigned the speaker for at least two sessions in a conference)

###Task #2 - Add Session to Wishlist
Wishlist endpoints were implemented as required. addSessionToWishlist(SessionKey), getSessionsInWishlist(), deleteSessionInWishlist(SessionKey)

A wishList repeated list property was added to the Profile model class and functionality was added to iterate a user's profile to get, add, or remove sessions from the wishlist if they had authorization.

###Task #3 - Indexes and additional two queries
Indexes added: All are automatically generated by the app. when queries are run as described in the index.yaml file comments.

Two additional queries added:

1. getConferenceSessionsByHighlights(websafeConferenceKey, highlights) - Retrieves conference sessions by highlight.
2. getProfileByEmail(mainEmail) - Allows conference organizer to retrieve a registered user's profile by entering an email address. It could be used to manually verify users in a conference or t-shirt size. This is more of a utility/admin function and could more useful in the future if more properties and user details, pictures, etc, are added to the profile.

###Task #4 - Implement getFeaturedSpeaker()

The endpoint retrieves a conference's featured speaker set in memcache from the SetFeaturedSpeaker task. Featured Speaker key is the user's email address. When a session is inserted, the task is run. It checks to see if the user is a speaker at any of the other conference sessions. If so, the memcache key is saved for the conference key and stores the user's speakerKey and session names. They are returned in the getFeaturedSpeaker endpoint.

###Task #5 - Query Related Problem

There is an issue because you want to query two properties. As stated in the documentation, you are limited to filtering one property at a time: [Inequality filters are limited to at most one property](https://cloud.google.com/appengine/docs/python/datastore/queries?hl=en#Python_Restrictions_on_queries)
* Solving this could be to query and filter one property, then iterate the results and remove the second query 'manually' in a loop.