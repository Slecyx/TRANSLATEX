from pdf2docx import Converter
from docx import Document
import subprocess
import os
from .translator import translate_text

def translate_pdf(input_path: str, output_path: str, target_lang: str, progress_callback=None):
    """
    Translates a PDF file to the target language via DOCX conversion.
    Returns the path to the final output file (PDF if possible, else DOCX).
    """
    # Step 1: Convert PDF to DOCX
    docx_path = input_path.replace('.pdf', '.docx')
    if os.path.exists(docx_path):
        os.remove(docx_path)
        
    cv = Converter(input_path)
    cv.convert(docx_path)
    cv.close()
    
    # Step 2: Translate DOCX content
    doc = Document(docx_path)
    
    total_items = len(doc.paragraphs) + sum(len(table.rows) for table in doc.tables)
    current_item = 0
    
    for para in doc.paragraphs:
        current_item += 1
        if progress_callback and current_item % 5 == 0:
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
                        
    translated_docx_path = output_path.replace('.pdf', '_translated.docx')
    doc.save(translated_docx_path)
    
    # Step 3: Convert back to PDF using LibreOffice (if available)
    try:
        # Check if libreoffice is available
        subprocess.run(['libreoffice', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Convert to PDF
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', translated_docx_path, '--outdir', os.path.dirname(output_path)], check=True)
        
        # The output file will have same name as translated_docx_path but with .pdf estension
        expected_pdf_path = translated_docx_path.replace('.docx', '.pdf')
        
        if os.path.exists(expected_pdf_path):
             # Rename to desired output path
            if os.path.exists(output_path):
                os.remove(output_path)
            os.rename(expected_pdf_path, output_path)
            return output_path
        else:
             print("LibreOffice conversion failed silently, returning DOCX.")
             return translated_docx_path

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("LibreOffice not found or failed. Returning translated DOCX.")
        return translated_docx_path
