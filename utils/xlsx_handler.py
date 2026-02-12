import openpyxl
from .translator import translate_text

def translate_xlsx(input_path: str, output_path: str, target_lang: str):
    """Translates an XLSX file to the target language."""
    wb = openpyxl.load_workbook(input_path)
    
    for sheet in wb.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str) and cell.value.strip():
                    cell.value = translate_text(cell.value, target_lang)
                    
    wb.save(output_path)
    return output_path
