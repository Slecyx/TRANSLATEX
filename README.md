# 🌌 TranslateX Prime | Next-Gen AI Document Localization

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

### [English] 🇺🇸

**TranslateX Prime** is an ultra-modern, sci-fi inspired document localization engine. It leverages advanced AI models to translate documents while preserving their original layout and formatting. Built with a focus on speed, aesthetics, and usability.

#### ✨ Key Features
- **Hyper-Premium UI:** Immersive dark mode, neon accents, and animated backgrounds.
- **Universal Format Support:**
  - 📄 **PDF** (Automatic Layout Preservation)
  - 📊 **PPTX** (PowerPoint Presentations - with optional PDF rendering)
  - 📝 **DOCX** (Word Documents)
  - 📉 **XLSX** (Excel Spreadsheets)
  - 📜 **TXT** (Plain Text)
- **🚀 High-Performance Core:** Multithreaded batch processing for 10x faster translations.
- **📦 Smart Conversion:** Automatically handles PDF conversion using system tools or Flatpak wrappers (LibreOffice).
- **🔒 Secure & Local:** Files are processed locally/temporarily and deleted immediately after the session.

#### 🛠️ Installation & Usage

**Prerequisites:**
- Python 3.8+
- LibreOffice (for optimal PDF/PPTX conversion)

**1. Clone the Repository:**
```bash
git clone https://github.com/Slecyx/TRANSLATEX.git
cd TRANSLATEX
```

**2. Set Up Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the System:**
```bash
streamlit run app.py
```
Access the interface at `http://localhost:8501`.

---

### [Türkçe] 🇹🇷

**TranslateX Prime**, bilim kurgu estetiğine sahip, ultra modern bir doküman çeviri motorudur. Orijinal belge düzenini koruyarak gelişmiş yapay zeka modelleriyle çeviri yapar. Hız, estetik ve kullanım kolaylığı odaklı geliştirilmiştir.

#### ✨ Temel Özellikler
- **Hyper-Premium Arayüz:** Etkileyici karanlık mod, neon detaylar ve animasyonlu arka planlar.
- **Evrensel Format Desteği:**
  - 📄 **PDF** (Otomatik Düzen Koruma)
  - 📊 **PPTX** (PowerPoint Sunumları - isteğe bağlı PDF çıktısı)
  - 📝 **DOCX** (Word Belgeleri)
  - 📉 **XLSX** (Excel Tabloları)
  - 📜 **TXT** (Düz Metin)
- **🚀 Yüksek Performanslı Çekirdek:** Çoklu iş parçacığı (multithreading) ile 10 kat daha hızlı çeviri.
- **📦 Akıllı Dönüştürme:** PDF dönüşümleri için sistemdeki veya Flatpak üzerindeki LibreOffice'i otomatik kullanır.
- **🔒 Güvenli & Yerel:** Dosyalar geçici olarak işlenir ve oturum bitiminde silinir.

#### 🛠️ Kurulum ve Kullanım

**Gereksinimler:**
- Python 3.8+
- LibreOffice (En iyi PDF/PPTX dönüşümü için gereklidir - `sudo apt install libreoffice`)

**1. Projeyi Klonlayın:**
```bash
git clone https://github.com/Slecyx/TRANSLATEX.git
cd TRANSLATEX
```

**2. Sanal Ortamı Hazırlayın:**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

**3. Bağımlılıkları Yükleyin:**
```bash
pip install -r requirements.txt
```

**4. Sistemi Başlatın:**
```bash
streamlit run app.py
```
Arayüze `http://localhost:8501` adresinden erişebilirsiniz.

---

## 📂 Project Structure / Proje Yapısı

```
TRANSLATEX/
├── app.py                  # Main Application Core
├── requirements.txt        # Dependency Manifest
├── Procfile                # Deployment Config
├── run.sh                  # Quick Launcher
├── utils/
│   ├── translator.py       # AI Translation Engine (Multithreaded)
│   ├── pptx_handler.py     # PowerPoint Processor
│   ├── pdf_handler.py      # PDF Processor (w/ Flatpak support)
│   ├── docx_handler.py     # Word Document Processor
│   ├── xlsx_handler.py     # Spreadsheet Processor
│   └── txt_handler.py      # Text File Processor
├── .streamlit/
│   └── config.toml         # UI Configuration
└── LICENSE                 # GPLv3 License
```

## 🤝 Contribution / Katkı
Open source forever. Pull requests are welcome to improve the core logic or UI.
Açık kaynak geliştirme. Kod mantığını veya arayüzü geliştirmek için Pull Request gönderebilirsiniz.

## 📄 License
Licensed under the **GPLv3** License. See [LICENSE](LICENSE) for details.

---
<p align="center">System Architect: Slecyx // End of Line.</p>
