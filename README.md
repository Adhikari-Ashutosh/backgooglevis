👋 Hi,
This repository contains a Python program that has a POST endpoint configured with CORS to trigger the google cloud vision api!
There's not many projects that do this so might be useful if you are using google API's with flask.
---

# Deployment: 


Run the following commands in your cloud console:
- <code>git clone https://github.com/Adhikari-Ashutosh/backgooglevis/</code> - replace this with your own github link if you need to
- <code>cd YOUR_DIR_NAME</code> - Navigate to the new folder
- <code>gcloud app deploy</code>
---
# Linking structure:

There's two main links that the program provides
- <code>/</code>- default testing link, Just a hello world to see if your server is up.
- <code>/test</code>- a post endpoint that accepts b64 png data as input and returns JSON containing the most likely label for provided image.
---

# Original Usecase:

Honestly, I didn't know react REST API's that well and I didn't want to risk exposing my API keys's to the public domain, hence I built this application 
as a service that helps me use my react application to trigger this service (hosted in a different place). Also wanted to learn about the Google app engine.
---

# Thank you for Reading!
Lemme know if you have any doubts regarding this!
