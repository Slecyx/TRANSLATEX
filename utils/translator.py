from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str) -> str:
    """Translates text to the target language using Google Translate."""
    if text is None:
        return ""
    
    if not isinstance(text, str):
        text = str(text)

    if not text.strip():
        return text
    
    try:
        # Check if text is too long (Google Translate limit is around 5000 chars)
        if len(text) > 4000:
            # Simple chunking by newlines or blindly split
            translated_chunks = []
            for i in range(0, len(text), 4000):
                chunk = text[i:i+4000]
                result = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
                if result:
                     translated_chunks.append(result)
                else:
                     translated_chunks.append(chunk) # Fallback to original
            return "".join(translated_chunks)
        
        result = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return result if result is not None else text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text

def batch_translate_texts(texts: list, target_lang: str, max_workers=10):
    """
    Translates a list of texts in parallel using ThreadPoolExecutor.
    """
    if not texts:
        return []
    
    from concurrent.futures import ThreadPoolExecutor
    
    # We maintain order by mapping future to index or simply map
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda t: translate_text(t, target_lang), texts))
        
    return results
