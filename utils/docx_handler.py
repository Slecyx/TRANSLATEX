from docx import Document
from .translator import translate_text

def translate_docx(input_path: str, output_path: str, target_lang: str, progress_callback=None):
    """Translates a DOCX file to the target language."""
    doc = Document(input_path)
    
    # Calculate approximate total items (paragraphs + table rows)
    total_items = len(doc.paragraphs) + sum(len(table.rows) for table in doc.tables)
    current_item = 0

    for para in doc.paragraphs:
        current_item += 1
        if progress_callback and current_item % 5 == 0: # Update every 5 items to avoid overhead
            progress_callback(current_item, total_items)
            
        if para.text.strip():
            translated_text = translate_text(para.text, target_lang)
            para.text = translated_text
            
    for table in doc.tables:
        for row in table.rows:
            current_item += 1
            if progress_callback and current_item % 5 == 0:
                progress_callback(current_item, total_items)

            for cell in row.cells:
                for para in cell.paragraphs:
                    if para.text.strip():
                        translated_text = translate_text(para.text, target_lang)
                        para.text = translated_text
                        
    doc.save(output_path)
    return output_path
