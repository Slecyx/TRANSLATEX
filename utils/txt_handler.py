from .translator import translate_text

def translate_txt(input_path: str, output_path: str, target_lang: str, progress_callback=None):
    """Translates a TXT file to the target language with progress tracking."""
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    if not text:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("")
        return output_path
        
    chunk_size = 4000
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    total_chunks = len(chunks)
    translated_chunks = []
    
    for i, chunk in enumerate(chunks):
        if progress_callback:
            progress_callback(i + 1, total_chunks)
            
        translated_chunk = translate_text(chunk, target_lang)
        translated_chunks.append(translated_chunk)
    
    final_text = "".join(translated_chunks)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_text)
        
    return output_path
