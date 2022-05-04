
import ibm_watson

from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



from ibm_ai_modules import config_language

url_lt = config_language.url_lt
apikey_lt = config_language.apikey_lt
version_lt = config_language.version_lt


authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

# Check
language_translator




def french_to_english(recognized_text):
        translation_response_fr_engl = \
        language_translator.translate(\
        text=recognized_text, model_id='fr-en')
        translation_fr_engl=translation_response_fr_engl.get_result()
        engl_translation =translation_fr_engl['translations'][0]['translation']
        return engl_translation

french_to_english('Bonjour')