from googletrans import Translator

def TransLate(text, lang):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=lang).text
        return translated_text
    except Exception as e:
        return f"Translation error: {e}"

def LangDetect(txt):
    translator = Translator()
    try:
        detected = translator.detect(txt)
        return f"Detected(lang={detected.lang}, confidence={detected.confidence})"
    except Exception as e:
        return f"Language detection error: {e}"

def CodeLang(lang):
    return lang.lower()

if __name__ == "__main__":
    txt = "Доброго дня. Як справи?"
    lang = "en"
    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang(lang))
