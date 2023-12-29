from flask import Flask, jsonify, request
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.debug=True
load_dotenv()
client = OpenAI()

@app.route('/', methods=['POST'])
def home():
  client.api_key=os.getenv("OPENAI_API_KEY")
  mymessage = request.get_json()["prompt"]
  response = client.images.edit(
  model="dall-e-2",
  image=open("capture.png", "rb"),
  mask=open("captures.png", "rb"),
  prompt=mymessage,
  n=1,
  size="1024x1024"
)

  return jsonify({"url":response.data[0].url})

if __name__ == '__main__':
     app.run()
