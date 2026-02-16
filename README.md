# PDF AI Chatbot using Python, OCR & LLMs

This project is a Python-based AI chatbot that allows users to ask questions from PDF documents. 
It supports both text-based PDFs and scanned PDFs using OCR. 

I create this project to understand how real-world AI applications handle document reading,OCR,and question answering together.

# Features
-Ask questions from PDF documents
-Works with text-based PDFs
-Works with scanned PDFs using OCR
-Automatically detects when OCR is required
-Clean and simple command-line interface
-Environment variable support for API security

# Technologies Used
-Python
-PyPDF2 (for reading text PDFs)
-pytesseract (OCR for scanned PDFs)
-Pillow (image processing)
-Groq API (AI responses)
-python-dotenv (environment variables
---
# Project Structure
pdf_ai_chatbot/
│── main.py
│── pdf_reader.py
│── ocr_utils.py
│── requirements.txt
│── README.md
│── sample.pdf
│── .gitignore

# How It Works
I built this project to learn how AI models can be combined with OCR and PDF processing 
to create a practical document question-answering system.

1 User provides a PDF file
2 The program checks whether the PDF contains readable text
3 If text is found → PyPDF2 is used
4 If no text is found → OCR is applied using Tesseract
5 Extracted text is sent to the AI model
6 AI generates answers based on the PDF content

# Setup Instructions
 1️.Clone the repository
```bash
git clone https://github.com/your-username/pdf_ai_chatbot.git
cd pdf_ai_chatbot

2️.Install dependencies
pip install -r requirements.txt

3️.Create .env file
Create a file named .env and add:
GROQ_API_KEY=your_api_key_here

4️.Run the project
python main.py

# Sample PDF
The repository includes a sample PDF for testing.
You can also use your own text-based or scanned PDFs.

# Future Enhancements
-Web interface (Streamlit / Flask)
-Upload multiple PDFs
-Save chat history
-Better error handling

# Author
Monali Yenchalwar
Aspiring Python & AI Developer
India