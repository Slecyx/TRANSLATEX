import streamlit as st
import os
import tempfile
import traceback
import time
import base64
from datetime import datetime
from utils.pptx_handler import translate_pptx, convert_pptx_to_pdf
from utils.pdf_handler import translate_pdf
from utils.docx_handler import translate_docx
from utils.txt_handler import translate_txt
from utils.xlsx_handler import translate_xlsx

# --- Cloud Config ---
st.set_page_config(
    page_title="TranslateX Prime | AI Suite",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Session State for Mission Log ---
if 'history' not in st.session_state:
    st.session_state['history'] = []

def add_to_history(filename, lang, status, time_taken):
    st.session_state['history'].insert(0, {
        "time": datetime.now().strftime("%H:%M:%S"),
        "file": filename,
        "lang": lang,
        "status": status,
        "duration": f"{time_taken:.1f}s"
    })

# --- Hyper-Premium CSS ---
def add_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;500;700&display=swap');

        /* === ANIMATED BACKGROUND === */
        .stApp {
            background: #000000;
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(76, 29, 149, 0.2) 0%, rgba(0, 0, 0, 0) 50%),
                linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)),
                url("https://www.transparenttextures.com/patterns/cubes.png");
            overflow-x: hidden;
            font-family: 'Rajdhani', sans-serif;
        }

        /* Moving Grid Animation */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0; left: 0; width: 200vw; height: 200vh;
            background: 
                linear-gradient(transparent 0%, rgba(0, 255, 255, 0.03) 50%, transparent 100%),
                linear-gradient(90deg, transparent 0%, rgba(255, 0, 255, 0.03) 50%, transparent 100%);
            background-size: 100px 100px;
            animation: moveGrid 20s linear infinite;
            z-index: -1;
            transform: perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px);
            pointer-events: none;
        }

        @keyframes moveGrid {
            0% { transform: perspective(500px) rotateX(60deg) translateY(0) translateZ(-200px); }
            100% { transform: perspective(500px) rotateX(60deg) translateY(100px) translateZ(-200px); }
        }

        /* === TYPOGRAPHY === */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        /* === HERO SECTION === */
        .hero-container {
            text-align: center;
            padding: 3rem 1rem;
            position: relative;
        }
        
        .hero-title {
            font-size: 4.5rem;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0px 0px 20px rgba(0, 198, 255, 0.5);
            margin-bottom: 0px;
            animation: glow 3s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 10px rgba(0, 198, 255, 0.5); }
            to { text-shadow: 0 0 30px rgba(0, 114, 255, 0.8), 0 0 10px rgba(0, 255, 255, 0.8); }
        }

        .hero-subtitle {
            font-size: 1.2rem;
            color: #a0a0ba;
            letter-spacing: 3px;
            margin-top: -10px;
            opacity: 0.8;
        }

        /* === GLASS CARD === */
        .glass-card {
            background: rgba(10, 10, 20, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(0, 255, 255, 0.1);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
            transition: all 0.4s ease;
            margin-bottom: 2rem;
        }

        /* === FILE UPLOADER === */
        .stFileUploader {
            border: 1px dashed rgba(0, 255, 255, 0.3);
            border-radius: 8px;
            padding: 15px;
            background: rgba(0,0,0,0.3);
        }

        /* === BUTTONS === */
        .stButton > button {
            background: transparent;
            border: 1px solid #00c6ff;
            color: #00c6ff;
            font-size: 1rem;
            font-weight: 700;
            padding: 0.6rem 2rem;
            border-radius: 4px;
            transition: all 0.3s ease;
            text-transform: uppercase;
            width: 100%;
            letter-spacing: 1px;
        }

        .stButton > button:hover {
            background: rgba(0, 198, 255, 0.1);
            color: #fff;
            box-shadow: 0 0 15px rgba(0, 198, 255, 0.4);
            border-color: #fff;
        }

        /* === DOWNLOAD BUTTON === */
        .stDownloadButton > button {
            background: linear-gradient(90deg, #ff0099, #493240);
            border: none;
            color: white;
            font-size: 1rem;
            padding: 0.8rem 2rem;
            border-radius: 4px;
            box-shadow: 0 4px 15px rgba(255, 0, 153, 0.2);
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .stDownloadButton > button:hover {
            box-shadow: 0 0 20px rgba(255, 0, 153, 0.6);
            color: #fff;
        }

        /* === LOG TABLE === */
        .log-table {
            width: 100%;
            border-collapse: collapse;
            color: #a0a0ba;
            font-size: 0.9rem;
        }
        .log-table th {
            text-align: left;
            border-bottom: 1px solid rgba(0, 255, 255, 0.2);
            padding: 8px;
            color: #00c6ff;
        }
        .log-table td {
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding: 8px;
        }
        .log-status-success { color: #00ff99; }
        .log-status-fail { color: #ff0055; }

        /* === CHECKBOX === */
        .stCheckbox {
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 8px;
            border: 1px dashed rgba(0, 255, 255, 0.3);
            margin-top: 10px;
            color: #fff;
        }
        .stCheckbox > label {
            color: #e0e0e0;
            font-size: 0.9rem;
            letter-spacing: 1px;
        }

        /* Hiding Default Elements */
        #MainMenu, footer, header { visibility: hidden; }
        
    </style>
    """, unsafe_allow_html=True)

def main():
    add_custom_css()

    st.markdown('<div class="hero-container"><div class="hero-title">TRANSLATEX</div><div class="hero-subtitle">SYSTEM VERSION 4.1 // READY</div></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📥 DATA INGESTION")
        
        uploaded_file = st.file_uploader("DROP FILE HERE", type=["pdf", "pptx", "docx", "txt", "xlsx"])
        
        # Advanced Toggle for PPTX
        convert_to_pdf_opt = False
        if uploaded_file and uploaded_file.name.lower().endswith(".pptx"):
            st.markdown("---")
            convert_to_pdf_opt = st.checkbox("� RENDER PPTX AS PDF", value=False)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### ⚙️ PARAMETERS")
        
        lang_options = {
            "tr": "🇹🇷 TURKISH", "en": "🇺🇸 ENGLISH", "de": "🇩🇪 GERMAN", 
            "fr": "🇫🇷 FRENCH", "es": "🇪🇸 SPANISH", "it": "🇮🇹 ITALIAN", 
            "ru": "🇷🇺 RUSSIAN", "ar": "🇸🇦 ARABIC", "ja": "🇯🇵 JAPANESE", "ko": "🇰🇷 KOREAN"
        }
        
        target_language = st.selectbox(
            "TARGET SYNTAX",
            options=list(lang_options.keys()),
            format_func=lambda x: lang_options[x]
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if uploaded_file:
            process_btn = st.button("🚀 INITIATE SEQUENCE")
        else:
            st.button("� AWAITING INPUT", disabled=True)
            process_btn = False
            
        st.markdown("</div>", unsafe_allow_html=True)

    # Processing Logic
    if process_btn and uploaded_file:
        with st.empty():
            st.markdown('<div class="glass-card" style="text-align:center;">Initializing Protocol...</div>', unsafe_allow_html=True)
            progress_bar = st.progress(0)
            status_text = st.empty()
            timer_text = st.empty()
            
            start_time = time.time()
            
            def update_progress(current, total):
                if total == 0:
                    percent = 0
                else:
                    percent = int((current / total) * 100)
                
                progress_bar.progress(min(percent, 100))
                
                elapsed_time = time.time() - start_time
                if current > 0:
                    avg_time_per_item = elapsed_time / current
                    remaining_items = total - current
                    est_remaining_time = avg_time_per_item * remaining_items
                    
                    status_text.markdown(f"""
                        <div class="glass-card" style="text-align:center; padding: 1rem; margin-top: 10px;">
                            <div style="margin-bottom: 5px; color: #00c6ff; font-weight: bold; font-family: 'Orbitron', sans-serif;">
                                ⏳ PROCESSING: {current}/{total} SEGMENTS ({percent}%)
                            </div>
                            <div style="font-size: 0.85rem; color: #a0a0ba;">
                                ⏱️ ELAPSED: {elapsed_time:.1f}s | EST. REMAINING: {est_remaining_time:.1f}s
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    status_text.markdown("""
                        <div class="glass-card" style="text-align:center; padding: 1rem; margin-top: 10px;">
                            <div style="color: #a0a0ba;">⏳ INITIALIZING SEQUENCE...</div>
                        </div>
                    """, unsafe_allow_html=True)

            try:
                # Clear previous result
                if 'latest_result' in st.session_state:
                    del st.session_state['latest_result']

                status_text.text("⚡ NEURAL LINK ESTABLISHED")
                time.sleep(0.3)
                
                # Save uploaded file
                file_ext = uploaded_file.name.split('.')[-1].lower()
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    input_path = tmp_file.name
                
                output_path = input_path.replace(f".{file_ext}", f"_translated.{file_ext}")
                
                # Translate
                if file_ext == "pptx":
                    result_path = translate_pptx(input_path, output_path, target_language, progress_callback=update_progress)
                    progress_bar.progress(100)
                    if convert_to_pdf_opt:
                            status_text.text("📄 COMPILLING PDF ARTIFACT...")
                            pdf_path = output_path.replace('.pptx', '.pdf')
                            converted_pdf = convert_pptx_to_pdf(result_path, pdf_path)
                            if converted_pdf:
                                result_path = converted_pdf
                elif file_ext == "pdf":
                    convert_to_pdf = (pdf_output_format == "PDF")
                    result_path = translate_pdf(input_path, output_path, target_language, progress_callback=update_progress, convert_to_pdf=convert_to_pdf)
                elif file_ext == "docx":
                    result_path = translate_docx(input_path, output_path, target_language, progress_callback=update_progress)
                elif file_ext == "txt":
                    result_path = translate_txt(input_path, output_path, target_language, progress_callback=update_progress)
                elif file_ext == "xlsx":
                    # XLSX support needs to be updated for callbacks, for now just pass without
                    status_text.text("📊 PROCESSING SPREADSHEET DATA...")
                    result_path = translate_xlsx(input_path, output_path, target_language) 
                else:
                    raise ValueError("Unsupported Format")

                progress_bar.progress(100)
                total_duration = time.time() - start_time
                status_text.text(f"✅ SEQUENCE COMPLETE ({total_duration:.1f}s)")
                timer_text.empty()
                time.sleep(0.5)
                
                # Add to history
                add_to_history(uploaded_file.name, target_language.upper(), "SUCCESS", total_duration)

                # Prepare Download Data
                with open(result_path, "rb") as f:
                    file_data = f.read()
                    
                download_name = uploaded_file.name.replace(".", f"_{target_language}.")
                final_ext = result_path.split('.')[-1]
                if not download_name.endswith(f".{final_ext}"):
                        download_name = ".".join(download_name.split('.')[:-1]) + f".{final_ext}"

                mime_type = "application/octet-stream"
                
                # Store in session state for persistence
                st.session_state['latest_result'] = {
                    "data": file_data,
                    "name": download_name,
                    "mime": mime_type
                }
                
                st.balloons()
                
            except Exception as e:
                st.error("SEQUENCE FAILURE")
                add_to_history(uploaded_file.name, target_language.upper(), "FAILED", time.time() - start_time)
                st.code(traceback.format_exc())
            finally:
                if 'input_path' in locals() and os.path.exists(input_path): os.remove(input_path)
                if 'result_path' in locals() and os.path.exists(result_path): os.remove(result_path)

    # --- PERSISTENT DOWNLOAD AREA ---
    if 'latest_result' in st.session_state:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col_res1, col_res2 = st.columns([3, 1])
        with col_res1:
            st.success(f"READY FOR EXTRACTION: {st.session_state['latest_result']['name']}")
        with col_res2:
            st.download_button(
                label="⬇️ ACQUIRE ASSET",
                data=st.session_state['latest_result']['data'],
                file_name=st.session_state['latest_result']['name'],
                mime=st.session_state['latest_result']['mime']
            )
        st.markdown('</div>', unsafe_allow_html=True)

    # --- MISSION LOG ---
    if st.session_state['history']:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📜 MISSION LOG")
        
        table_html = '<table class="log-table"><thead><tr><th>TIME</th><th>FILE</th><th>LANG</th><th>STATUS</th><th>DURATION</th></tr></thead><tbody>'
        
        for item in st.session_state['history']:
            status_class = "log-status-success" if item['status'] == "SUCCESS" else "log-status-fail"
            table_html += f"<tr><td>{item['time']}</td><td>{item['file']}</td><td>{item['lang']}</td><td class='{status_class}'>{item['status']}</td><td>{item['duration']}</td></tr>"
        
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("<div style='text-align: center; color: #444; margin-top: 50px; font-size: 0.8em;'>SECURE TERMINAL ACCESS // ENCRYPTED</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
