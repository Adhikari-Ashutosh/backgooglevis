from flask import Flask
# from google.cloud import vision
# print("Test1")
app = Flask(__name__)
# client = vision.ImageAnnotatorClient()
@app.route("/")
def testAPI():
    return "<p>Hello, World!</p>"
@app.route("/test")
def checkMic():
    pass

if __name__ == "__main__":
   app.run()