from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('7fXqhg4K0w4n_9IA_SEuBnRV0X7-xE5Ph7ajPOF4F8-7')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/46fe4c55-19eb-4149-9edc-8fa02bf29a7a')


def english_to_french(english_text):
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text


# print(english_to_french('Hello. How are you today?'))
# print(french_to_english("Bonjour. Comment es-tu aujourd'hui?"))
