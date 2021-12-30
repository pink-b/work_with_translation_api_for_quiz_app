from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = "BU6SVBxw_lTL9l4uUygiM9-ooP2OhyMZnKQwscPK0XCt"
uri = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/60d2fe13-8722-4f33-9569-3d1943f74dd1"

authenticator = IAMAuthenticator(apikey)
it = LanguageTranslatorV3(version = '2018-05-01', authenticator = authenticator)
it.set_service_url(uri)

translation = it.translate(text='Who painted &quot;Swans Reflecting Elephants&quot;, &quot;Sleep&quot;, and &quot;The Persistence of Memory&quot;?', model_id='en-ru').get_result()
print(translation)
