import argparse
from translate import Translator

parser = argparse.ArgumentParser(description = "Translator")
parser.add_argument("-FL","--from_lang", required=True, metavar="", help="From what language we need translation")
parser.add_argument("-TL","--to_lang",required=True, metavar="",help="Language to translate (by default it will Engllish)")
args = parser.parse_args()
text = input("Enter a text to translate : ")

if args.from_lang :
    translator = Translator(
        to_lang = args.to_lang if args.to_lang else "English", 
        from_lang = args.from_lang
    )
else:
    translator = Translator(
        to_lang = args.to_lang if args.to_lang else "English"
    )
try:
    translation = translator.translate(text)
except Exception:
    print("Translation error...")
    
print(translation)