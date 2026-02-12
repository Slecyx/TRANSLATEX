from docx import Document
from .translator import translate_text

def translate_docx(input_path: str, output_path: str, target_lang: str):
    """Translates a DOCX file to the target language."""
    doc = Document(input_path)
    
    for para in doc.paragraphs:
        if para.text.strip():
            translated_text = translate_text(para.text, target_lang)
            para.text = translated_text
            
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    if para.text.strip():
                        translated_text = translate_text(para.text, target_lang)
                        para.text = translated_text
                        
    doc.save(output_path)
    return output_path
