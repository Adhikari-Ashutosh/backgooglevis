from flask import Flask
from google.cloud import vision
print("Test1")
app = Flask(__name__)
client = vision.ImageAnnotatorClient()
@app.route("/" , methods=['POST'])
def testAPI():
    image_uri = request.json.get('image_uri')
    response = client.annotate_image({
  'image': {'source': {'image_uri': image_uri}},
  'features': [{'type_': vision.Feature.Type.LABEL_DETECTION}]
        })
    print(response)
    return response
@app.route("/test")
def checkMic():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80)