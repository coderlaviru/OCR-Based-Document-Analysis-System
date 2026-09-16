# Deep Learning OCR Document Analysis System

An **AI-powered OCR and document analysis system** designed to seamlessly extract and analyze text from images, PDFs, and Word documents. Built with a Streamlit interface, this application leverages advanced deep learning frameworks including **PaddleOCR**, **EasyOCR**, and **OpenCV** to preprocess inputs and generate structured text outputs efficiently.

---

## 🚀 Features
* **Multi-Format Support:** Process Images (`.jpg`, `.jpeg`, `.png`), PDFs (`.pdf`), and Word documents (`.docx`).
* **Advanced Preprocessing:** Integrated OpenCV workflows to enhance image quality and maximize text extraction accuracy.
* **Robust OCR Engine:** Powered by PaddleOCR and EasyOCR for high-fidelity text recognition across diverse document types.
* **Automated PDF Workflows:** Automatically converts multi-page PDFs to image streams for pipeline execution.
* **Structured Output Export:** View extracted text inside an interactive UI text area and automatically save outputs as structured text files.

---

## 🛠️ Project Structure
```text
OCR-Based-Document-Analysis-System/
│
├── ocr_engine/                 # Core Deep Learning OCR configurations
│   ├── __init__.py
│   ├── paddle_ocr.py          # PaddleOCR initialization & inference pipelines
│   └── text_extractor.py      # Logic for text parsing and output file creation
│
├── preprocessing/              # CV preprocessing & document transformation pipelines
│   ├── __init__.py
│   ├── docx_reader.py          # Word document text mining utility
│   ├── image_preprocess.py     # Custom OpenCV filters (thresholding, noise reduction)
│   └── pdf_converter.py        # Multi-page PDF to rasterized image stream engine
│
├── utils/                      # Shared helper modules
│   ├── __init__.py
│   └── file_handler.py         # Secure upload operations & strict file extension routing
│
├── results/                    # Default runtime target directory for structured text file logs
│
├── .gitignore                  # Environment, virtual environment, and system file exclusion rules
├── LICENSE                     # MIT Open Source License distribution parameters
├── ocr_engine.zip              # Pre-packaged archive containing core model modules
└── final.zip                   # Master deployable backup containing application assets

```

---

## 🔧 Installation & Setup

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com
cd OCR-Based-Document-Analysis-System
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Ensure you have your `requirements.txt` ready, then run:
```bash
pip install -r requirements.txt
```
*Note: Make sure your requirements file includes packages like `streamlit`, `paddleocr`, `easyocr`, `opencv-python-headless`, and `python-docx`.*

---

## 💻 Usage

To launch the interactive dashboard, run the following command in your terminal:
```bash
streamlit run appModel.py
```

### How to use the Web App:
1. Open the local URL provided by Streamlit (usually `http://localhost:8501`).
2. **Upload** any supported file type (`pdf`, `jpg`, `png`, `jpeg`, `docx`).
3. For images and PDFs, the system automatically applies custom **OpenCV preprocessing algorithms** before executing the OCR engine.
4. View the parsed results inside the **OCR Output** text area. 
5. The processed data is automatically saved locally, confirming the structured file path upon completion.

---

## 🐳 Docker Deployment

The application includes a `Docker/` configuration directory for easy containerization. 

```bash
# Build the Docker image
docker build -t ocr-document-system -f Docker/Dockerfile .

# Run the container
docker run -p 8501:8501 ocr-document-system
```

---

## 📜 License
Distributed under the **MIT License**. See the `LICENSE` file for more details.

---

## 🤝 Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. 
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
