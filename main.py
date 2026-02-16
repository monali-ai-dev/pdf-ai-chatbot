import os
from dotenv import load_dotenv
from groq import Groq
from pdf_reader import read_pdf
from ocr_utils import perform_ocr

#LOAD ENV
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file.")

client = Groq(api_key=API_KEY)

#HISTORY FILE
history_file = "history.txt"
with open(history_file, "a", encoding="utf-8") as f:
    f.write("\n==== New Session Started ====\n")

#STEP 1: GET PDF
pdf_path = input("Enter your PDF file name or full path: ").strip().strip('"')

pages_text = read_pdf(pdf_path)   #MUST return list of page texts
final_text = ""

if not isinstance(pages_text, list):
    raise TypeError("read_pdf() must return a list of page texts")


for i, page_text in enumerate(pages_text):
    if page_text and page_text.strip():
        final_text += page_text + "\n"
    else:
        print(f"OCR running on page {i + 1}...")
        ocr_text = perform_ocr(pdf_path, page_number=i)
        final_text += ocr_text + "\n"

pdf_text = final_text
print("\n✅ PDF loaded successfully\n")

# MENU SYSTEM 
while True:
    print("\nMENU:")
    print("1. Ask question")
    print("2. View history")
    print("3. Summarize PDF")
    print("4. Exit")

    choice = input("Choose option (1/2/3/4): ").strip()

    if choice == "4":
        print("\n✅ Session ended. Answers saved in history.txt")
        break

    elif choice == "2":
        print("\n==== CHAT HISTORY ====")
        with open(history_file, "r", encoding="utf-8") as f:
            print(f.read())
        continue

    elif choice == "1":
        question = input("\nAsk a question from this PDF: ").strip()

        prompt = f"""
        You are a helpful assistant.
        Answer ONLY using the PDF content below.
        If the answer is not present, say exactly:
        "Answer not found in PDF."

        PDF CONTENT:
        {pdf_text}

        QUESTION:
        {question}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        answer = response.choices[0].message.content.strip()

        print("\n🤖 ANSWER:\n")
        print(answer)

        # Save to history
        with open(history_file, "a", encoding="utf-8") as f:
            f.write("\nQ: " + question + "\n")
            f.write("A: " + answer + "\n")
            f.write("------------------------------\n")
            
    elif choice == "3":
        print("\n⏳ Generating summary...")

        summary_prompt = f"""
        Summarize the following PDF in 5 clear bullet points:

        {pdf_text}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": summary_prompt}],
            temperature=0
        )

        summary = response.choices[0].message.content.strip()

        print("\n📄 PDF SUMMARY:\n")
        print(summary)

        # Save summary in history
        with open(history_file, "a", encoding="utf-8") as f:
            f.write("\n=== PDF SUMMARY ===\n")
            f.write(summary + "\n")
            f.write("------------------------------\n")

              
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
