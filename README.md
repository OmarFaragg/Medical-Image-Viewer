To run both servers:

 - install requirements.txt for Api app.
 - run "python main.py" for api server.
 - run "npm start" for frontend server.

# Medical-Image-Viewer

POST     /5000/signup  Signup functionality.

POST     /5000/login  Login functionality.

POST     /5000/logout/  Logout functionality.

POST     /5000/upload/  Upload the file and encrpt its data and assign it to the user and save it on the server.

POST     /5000/view/:id   Download and decrypt the specified file and view it.

POST     /3000/   signup and signin page.

POST     /3000/upload   Upload image page.

POST    /3000/view  View Dicom files page.


------------------------------------------------------
Security Design Measures:
- I implemented authentication to allow only user to access their previously uploaded files and also since files security is of high calibre I encrypted medical files on the server using AES encryption while generating the key uniquely from each user's hashed password to increase the security.
-----------------------------------------------------
Some backend Apis are created that is not yet connected to the frontend app.

