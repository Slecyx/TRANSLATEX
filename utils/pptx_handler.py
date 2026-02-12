import subprocess
import os
from pptx import Presentation
from .translator import translate_text

def convert_pptx_to_pdf(pptx_path: str, output_pdf_path: str):
    """Converts a PPTX file to PDF using LibreOffice."""
    try:
        # Check if libreoffice is available
        subprocess.run(['libreoffice', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        output_dir = os.path.dirname(output_pdf_path)
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', pptx_path, '--outdir', output_dir], check=True)
        
        # LibreOffice saves with the same basename but .pdf extension
        expected_output = pptx_path.replace('.pptx', '.pdf')
        
        if os.path.exists(expected_output):
            if expected_output != output_pdf_path:
                if os.path.exists(output_pdf_path):
                    os.remove(output_pdf_path)
                os.rename(expected_output, output_pdf_path)
            return output_pdf_path
        return None
    except Exception as e:
        print(f"Error converting PPTX to PDF: {e}")
        return None

def translate_pptx(input_path: str, output_path: str, target_lang: str, progress_callback=None):
    """Translates a PPTX file to the target language."""
    prs = Presentation(input_path)
    
    total_slides = len(prs.slides)
    for i, slide in enumerate(prs.slides):
        if progress_callback:
            progress_callback(i + 1, total_slides)
            
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.text.strip():
                        translated_text = translate_text(run.text, target_lang)
                        run.text = translated_text
                        
    prs.save(output_path)
    return output_path
