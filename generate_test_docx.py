from docx import Document

doc = Document()
doc.add_paragraph("Hello, OnlyOffice from Flatpak!")
doc.save("test.docx")
print("test.docx created")
