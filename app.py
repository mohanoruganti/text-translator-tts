from flask import Flask, render_template, request
from gtts import gTTS
from googletrans import Translator
import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", audio_play=False)

@app.route('/translate', methods=["POST"])
def translate():
    text = request.form['text']
    lang = request.form['language']

    # Translate
    translator = Translator()
    translated = translator.translate(text, dest=lang)

    # Convert to speech
    tts = gTTS(text=translated.text, lang=lang)
    audio_path = "static/output.mp3"
    tts.save(audio_path)

    return render_template("index.html", translated_text=translated.text, audio_play=True)

if __name__ == '__main__':
    app.run(debug=True)
