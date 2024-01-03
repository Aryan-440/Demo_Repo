from googletrans import Translator


def translateor(text,target_language='hi'):
    translator=Translator()
    translation=translator.translate(text,dest=target_language)

    print(f"Original Text: {text}")
    print(f"Translated Text: {translation.text}")


text_2_translate="Hello how are you"
target_language='hi'
translateor(text_2_translate,target_language)
