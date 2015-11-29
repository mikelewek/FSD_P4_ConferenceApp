##Conference Organization App. - FSD Project 4

This application...

###The Repo. Contains the Following Files
-------------------------------------
 1. xxx.py - Contains...
 2. ...provided by Udacity.
 x. README.md

###How to Run the Application
-------------------------
<p>Python 2.7 and the endpoints module must be installed and configured.</p>

<pre>
    <code>$ pip install endpoints</code>
	<code>$ git clone https://github.com/mikelewek/FSD_P4_ConferenceApp.git</code>
	<code>$ cd FSD_P4_ConferenceApp</code>
</pre>

###Task 1 - Explanation of Design Choices
I created the Session class, SessionForm class, and Endpoints, passing in required variables in the project outline as well as the websafeConferenceKey.
An Endpoint and function was created to get all sessions (getConferenceSessions). The CONF_GET_REQUEST is set as the request message class and SessionForm is set as the response message class. 
