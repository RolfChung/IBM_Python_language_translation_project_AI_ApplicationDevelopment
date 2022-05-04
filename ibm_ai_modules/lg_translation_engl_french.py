
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




def english_to_french(recognized_text, lgt=language_translator):
        # lt_2 = eval(lt)
        translation_response_fr = \
        lgt.translate(text=recognized_text, model_id='en-fr')
        translation_fr=translation_response_fr.get_result()
        french_translation =translation_fr['translations'][0]['translation']
        return french_translation 

english_to_french('Hello')