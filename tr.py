from bs4 import BeautifulSoup, Comment
from googletrans import Translator
import re

def translate_html_to_farsi(input_file, output_file):
    # read html input
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    #  BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    translator = Translator()

    # 
    def translate_text(text):
        # 
        text = re.sub(r'\s+', ' ', text).strip()
        if text and not text.isdigit() and not all(char in ':/.' for char in text):
            try:
                return translator.translate(text, src='en', dest='fa').text
            except:
                return text
        return text

    # find and translate all texts 
    for element in soup.find_all(text=True):
        if element.parent.name not in ['script', 'style'] and not isinstance(element, Comment):
            translated_text = translate_text(element.string)
            element.string.replace_with(translated_text)

    # save output
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

input_file = 'input.html'
output_file = 'output.html'
translate_html_to_farsi(input_file, output_file)
print(f"translate complete - {output_file} ")