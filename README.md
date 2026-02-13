# 🌌 TranslateX Prime | Next-Gen AI Translation Engine

<div align="center">

![TranslateX](https://img.shields.io/badge/TranslateX-Prime-00c6ff?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMkw0IDIwSDIwTDEyIDJaIiBmaWxsPSIjMDBjNmZmIi8+PC9zdmc+)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg?style=for-the-badge)]()

**Ultra-modern AI-powered document translation system with sci-fi inspired UI**

[🚀 Quick Start](#-quick-installation) • [📖 Features](#-key-features) • [🌐 Türkçe](#-türkçe-dokümantasyon)

</div>

---

## 🇺🇸 English Documentation

### 🎯 Overview

**TranslateX Prime** is a cutting-edge document localization engine featuring:
- **Stunning Sci-Fi UI** with neon accents, animated backgrounds, and dark theme
- **AI-Powered Translation** preserving original formatting and layout
- **Multi-Format Support** for PDF, PPTX, DOCX, XLSX, and TXT files
- **Blazing Fast Performance** with multithreaded batch processing
- **Privacy-First Design** - all processing happens locally

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📄 **PDF Support** | Automatic layout preservation with intelligent text extraction |
| 📊 **PowerPoint (PPTX)** | Translate presentations with optional PDF output |
| 📝 **Word Documents (DOCX)** | Maintain formatting, styles, and structure |
| 📉 **Excel Spreadsheets (XLSX)** | Preserve formulas and cell formatting |
| 📜 **Plain Text (TXT)** | Simple and fast text translation |
| 🌍 **10+ Languages** | Turkish, English, German, French, Spanish, Italian, Russian, Arabic, Japanese, Korean |
| 🚀 **High Performance** | Multithreaded processing for 10x faster translations |
| 🎨 **Premium UI** | Immersive dark mode with cyberpunk aesthetics |
| 🔒 **Secure** | Local processing, automatic file cleanup |

### 🚀 Quick Installation

**One-command setup:**

```bash
git clone https://github.com/Slecyx/TRANSLATEX.git
cd TRANSLATEX
./setup.sh
```

**Manual installation:**

```bash
# 1. Clone repository
git clone https://github.com/Slecyx/TRANSLATEX.git
cd TRANSLATEX

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional but recommended) Install LibreOffice for PDF conversion
# Ubuntu/Debian: sudo apt install libreoffice
# macOS: brew install --cask libreoffice
```

### 🎮 Usage

**Start the application:**

```bash
./run.sh
# Or manually:
streamlit run app.py
```

**Access the interface:**
- Open your browser and navigate to `http://localhost:8501`
- Drag and drop your file or click "Browse files"
- Select target language
- Click **"🚀 INITIATE SEQUENCE"**
- Download your translated file!

**Desktop Application (Linux):**

```bash
./launch.sh  # Opens in app mode (no browser UI)
# Or create desktop shortcut:
cp FileTranslator.desktop ~/Desktop/
```

### 📂 Project Structure

```
TRANSLATEX/
├── app.py                  # Main Streamlit application
├── setup.sh                # Automated installation script
├── run.sh                  # Quick launcher
├── launch.sh               # Desktop app launcher (Chromium app mode)
├── requirements.txt        # Python dependencies
├── utils/                  # Translation handlers
│   ├── translator.py       # Core AI translation engine (multithreaded)
│   ├── pptx_handler.py     # PowerPoint processor
│   ├── pdf_handler.py      # PDF processor with layout preservation
│   ├── docx_handler.py     # Word document processor
│   ├── xlsx_handler.py     # Excel spreadsheet processor
│   └── txt_handler.py      # Plain text processor
├── .streamlit/
│   └── config.toml         # UI configuration
└── LICENSE                 # GPLv3 License
```

### 🔧 Requirements

- **Python 3.8+**
- **LibreOffice** (optional, for optimal PDF/PPTX conversion)
- **Internet connection** (for AI translation API)

### 🎨 Screenshots

*TranslateX Prime features a stunning cyberpunk-inspired interface with:*
- Animated grid backgrounds
- Neon blue/cyan color scheme
- Real-time progress tracking
- Mission log for translation history

---

## 🇹🇷 Türkçe Dokümantasyon

### 🎯 Genel Bakış

**TranslateX Prime**, son teknoloji bir belge çeviri motorudur:
- **Muhteşem Bilim Kurgu Arayüzü** - neon detaylar, animasyonlu arka planlar, karanlık tema
- **Yapay Zeka Destekli Çeviri** - orijinal formatı ve düzeni koruyarak
- **Çoklu Format Desteği** - PDF, PPTX, DOCX, XLSX ve TXT dosyaları
- **Yıldırım Hızı** - çok iş parçacıklı toplu işleme ile
- **Gizlilik Odaklı** - tüm işlemler yerel olarak gerçekleşir

### ✨ Temel Özellikler

| Özellik | Açıklama |
|---------|----------|
| 📄 **PDF Desteği** | Akıllı metin çıkarma ile otomatik düzen koruma |
| 📊 **PowerPoint (PPTX)** | İsteğe bağlı PDF çıktısı ile sunumları çevirin |
| 📝 **Word Belgeleri (DOCX)** | Biçimlendirme, stiller ve yapıyı koruyun |
| 📉 **Excel Tabloları (XLSX)** | Formülleri ve hücre biçimlendirmesini koruyun |
| 📜 **Düz Metin (TXT)** | Basit ve hızlı metin çevirisi |
| 🌍 **10+ Dil** | Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, İtalyanca, Rusça, Arapça, Japonca, Korece |
| 🚀 **Yüksek Performans** | 10 kat daha hızlı çeviri için çoklu iş parçacığı |
| 🎨 **Premium Arayüz** | Cyberpunk estetiği ile etkileyici karanlık mod |
| 🔒 **Güvenli** | Yerel işleme, otomatik dosya temizleme |

### 🚀 Hızlı Kurulum

**Tek komutla kurulum:**

```bash
git clone https://github.com/Slecyx/TRANSLATEX.git
cd TRANSLATEX
./setup.sh
```

**Manuel kurulum:**

```bash
# 1. Depoyu klonlayın
git clone https://github.com/Slecyx/TRANSLATEX.git
cd TRANSLATEX

# 2. Sanal ortam oluşturun
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. (İsteğe bağlı ama önerilir) PDF dönüşümü için LibreOffice kurun
# Ubuntu/Debian: sudo apt install libreoffice
# macOS: brew install --cask libreoffice
```

### 🎮 Kullanım

**Uygulamayı başlatın:**

```bash
./run.sh
# Veya manuel olarak:
streamlit run app.py
```

**Arayüze erişin:**
- Tarayıcınızı açın ve `http://localhost:8501` adresine gidin
- Dosyanızı sürükle-bırak yapın veya "Browse files"a tıklayın
- Hedef dili seçin
- **"🚀 INITIATE SEQUENCE"** butonuna tıklayın
- Çevrilmiş dosyanızı indirin!

**Masaüstü Uygulaması (Linux):**

```bash
./launch.sh  # Uygulama modunda açar (tarayıcı arayüzü olmadan)
# Veya masaüstü kısayolu oluşturun:
cp FileTranslator.desktop ~/Desktop/
```

### 📂 Proje Yapısı

```
TRANSLATEX/
├── app.py                  # Ana Streamlit uygulaması
├── setup.sh                # Otomatik kurulum scripti
├── run.sh                  # Hızlı başlatıcı
├── launch.sh               # Masaüstü uygulama başlatıcı (Chromium uygulama modu)
├── requirements.txt        # Python bağımlılıkları
├── utils/                  # Çeviri işleyicileri
│   ├── translator.py       # Çekirdek AI çeviri motoru (çoklu iş parçacığı)
│   ├── pptx_handler.py     # PowerPoint işleyici
│   ├── pdf_handler.py      # Düzen koruma ile PDF işleyici
│   ├── docx_handler.py     # Word belgesi işleyici
│   ├── xlsx_handler.py     # Excel tablosu işleyici
│   └── txt_handler.py      # Düz metin işleyici
├── .streamlit/
│   └── config.toml         # Arayüz yapılandırması
└── LICENSE                 # GPLv3 Lisansı
```

### 🔧 Gereksinimler

- **Python 3.8+**
- **LibreOffice** (isteğe bağlı, optimal PDF/PPTX dönüşümü için)
- **İnternet bağlantısı** (AI çeviri API'si için)

### 🎨 Ekran Görüntüleri

*TranslateX Prime, şu özelliklere sahip muhteşem bir cyberpunk esinli arayüze sahiptir:*
- Animasyonlu ızgara arka planları
- Neon mavi/camgöbeği renk şeması
- Gerçek zamanlı ilerleme takibi
- Çeviri geçmişi için görev günlüğü

---

## 🤝 Contribution / Katkıda Bulunma

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

Katkılarınızı bekliyoruz! Şunları yapabilirsiniz:
- 🐛 Hata bildirme
- 💡 Yeni özellik önerme
- 🔧 Pull request gönderme

## 📄 License / Lisans

Licensed under the **GPLv3** License. See [LICENSE](LICENSE) for details.

**GPLv3** Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

<div align="center">

**System Architect: [Slecyx](https://github.com/Slecyx)**

*End of Line.*

</div>
