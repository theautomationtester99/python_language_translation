import json
from deep_translator import GoogleTranslator

# from translate import Translator
#
# translator = Translator(to_lang="German")

with open('English_Bundle.json', encoding="utf8") as f:
    d = json.load(f)
    # print(d["jnj_app_header"])
    # translation = translator.translate(d["jnj_app_header"])
    # print(translation)
    for i, (key, value) in enumerate(d.items()):
        # translated = GoogleTranslator(source='auto', target='de').translate(value)
        # translated = GoogleTranslator(source='auto', target='te').translate(value)
        translated = GoogleTranslator(source='auto', target='it').translate(value)
        print(str(i) + " of " + str(len(d)))
        print(translated)
        d[key] = translated
        # print(value)
    print(d)
    # mydict = {k: str(v).encode("utf-8") for k, v in d.items()}
    with open("french_bundle.json", "w", encoding='utf8') as outfile:
        json.dump(d, outfile, ensure_ascii=False)
