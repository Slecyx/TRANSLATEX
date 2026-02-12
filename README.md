# 🌍 TranslateX | AI-Powered Document Translator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-ff4b4b.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**TranslateX** is a state-of-the-art document translation tool designed for seamless, layout-preserving translations. Built with Python and Streamlit, it offers an "Ultra-Premium" user experience with a futuristic design.

## ✨ Features

- **🎨 Ultra-Modern UI:** Glassmorphism design, animated interactions, and a dark-themed aesthetic.
- **📄 Multi-Format Support:**
  - **PDF** (Portable Document Format)
  - **PPTX** (PowerPoint Presentations)
  - **DOCX** (Word Documents)
  - **XLSX** (Excel Spreadsheets)
  - **TXT** (Plain Text)
- **🧠 AI Translation:** Powered by Google Translate for accurate and context-aware translations.
- **🔄 Smart Conversion:**
  - Automatic PDF -> DOCX -> PDF workflow for layout preservation.
  - Option to convert translated PPTX files to PDF.
- **🌍 Global Reach:** Supports 10+ major languages including Turkish, English, German, French, Spanish, and more.

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- [LibreOffice](https://www.libreoffice.org/) (Required for PDF conversions)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/translatex.git
    cd translatex
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

1.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
    *Or use the provided script:*
    ```bash
    ./run.sh
    ```

2.  **Navigate to** `http://localhost:8501` in your browser.

3.  **Upload** your document, **Select** the target language, and **Translate**!

## 📦 Dependencies

- `streamlit`
- `deep-translator`
- `python-pptx`
- `pdf2docx`
- `python-docx`
- `openpyxl`
- `opencv-python-headless`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
<p align="center">Made with ❤️ by Slecyx</p>
