from .translator import translate_text

def translate_txt(input_path: str, output_path: str, target_lang: str):
    """Translates a TXT file to the target language."""
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    translated_text = translate_text(text, target_lang)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(translated_text)
        
    return output_path
