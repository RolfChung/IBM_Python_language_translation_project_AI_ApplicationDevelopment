from ibm_ai_modules import translator
from ibm_ai_modules import settings
from flask import Flask, render_template, request
import json
import random, threading, webbrowser
from werkzeug.wrappers import Request, Response

import ibm_watson
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_ai_modules import config_language


url_lt = settings.DOMAIN
apikey_lt = settings.SECRET_KEY
version_lt = settings.VERSION


authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
# Check
language_translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(textToTranslate):
    #textToTranslate = request.args.get(textToTranslate)
    english_to_french_translation = translator.english_to_french(textToTranslate, lgt=language_translator)
    return english_to_french_translation


@app.route("/frenchToEnglish")
def frenchToEnglish(textToTranslate):
    #textToTranslate = request.args.get(textToTranslate)
    french_to_english_translation = translator.french_to_english(textToTranslate, lgt=language_translator)
    return french_to_english_translation


@app.route("/")
def renderIndexPage():
        # Write the code to render template
        # if __name__ == "__main__":
            # app.run(host="0.0.0.0", port=8080)
            
        if __name__ == '__main__':
            port = 5000 + random.randint(0, 999)
            url = "http://127.0.0.1:{0}".format(port)
            threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
            from werkzeug.serving import run_simple
            run_simple('localhost', port, app)    