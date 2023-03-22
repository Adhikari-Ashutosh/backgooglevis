from flask import Flask,request,Response,jsonify
import base64
from io import BytesIO
from PIL import Image
import requests 
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# client = vision.ImageAnnotatorClient()
@app.route("/")
def testAPI():
    return "<p>Hello, World!</p>"
@app.route("/test",methods = ['POST'])
@cross_origin()
def checkMic():
    data = request.form['pngstring']
    png_index = data.find("data:image/png;base64")
    png_base64_string = data[png_index+len("data:image/png;base64")+1:]
    png_bytes = base64.b64decode(png_base64_string)
    png_image = Image.open(BytesIO(png_bytes))

    # Convert PNG image to TIFF image
    tiff_bytes = BytesIO()
    png_image.save(tiff_bytes, format='TIFF')
    tiff_bytes.seek(0)

    # Convert TIFF image to base64 string
    tiff_base64_string = tiff_base64_string = base64.b64encode(tiff_bytes.read()).decode('utf-8')
    payload = {
  "requests": [
    {
      "inputConfig": {
        'content': str(tiff_base64_string),
        "mimeType": "image/tiff"
      },
      "features": [
        {
          "type": "LABEL_DETECTION"
        }
      ]
    }
  ]
}   
    f = open('key.txt','r')
    key = f.read()
    link = f'https://vision.googleapis.com/v1/files:annotate?key={key}'
    r = requests.post(link, 
                 headers={'Accept': 'application/json', 'Content-Type': 'application/json'},data =json.dumps(payload))
    
    sr = r.json()
    winner = sr['responses'][0]['responses'][0]['labelAnnotations'][0]['description']
    
    data = {
        'winner' : str(winner)
    }
    return jsonify(data)



if __name__ == "__main__":
   app.run()