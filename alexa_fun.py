from flask import Flask 
from flask_ask import Ask, statement, question, session, request 
import json
import jsonify 
import time
import unidecode
app = Flask(__name__)
ask = Ask(app,"/askmanchu")
quote_audio = {
  "version": "1.0",
  "response": {
    "directives": [
      {
        "type": "AudioPlayer.Play",
        "playBehavior": "REPLACE_ALL",
        "audioItem": {
          "stream": {
            "token": "this-is-a-token",
            "url": "https://s3.amazonaws.com/funnymedia/alexa/manchu_lk_manchi_correct.mp3",
            "offsetInMilliseconds": 0
          }
        }
      }
    ],
    "shouldEndSession": True
  }
}

once_more_audio = {
  "version": "1.0",
  "response": {
    "directives": [
      {
        "type": "AudioPlayer.Play",
        "playBehavior": "REPLACE_ALL",
        "audioItem": {
          "stream": {
            "token": "this-is-a-token",
            "url": "https://s3.amazonaws.com/funnymedia/alexa/manchu_lk_garram_correct.mp3",
            "offsetInMilliseconds": 0
          }
        }
      }
    ],
    "shouldEndSession": True
  }
}
def get_audio():
	pass
	# filled in later'

@app.route('/askmanchu')
def homepage():
	return "hi there, how ya doin?"

@ask.launch
def start_skill():
	welcome_message = "Do you wanna listen a quote from Manchu Lakshmi or once more from her"
	return question(welcome_message)
@ask.intent("QuoteIntent")
def get_quote_audio():
	#audio_file_quote = 'playing quote audio'
	print type(quote_audio)
	print request
	#quote_audio_string = jsonify(quote_audio)
	return json.dumps(quote_audio)
@ask.intent("OnceMoreIntent")
def once_more_intent():
	audio_file_once_more = 'playing once more audio'
	return json.dumps(once_more_audio)
if __name__ == '__main__':
	app.run(debug=True)


