
import PyPDF2

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        try:
            text += page.extract_text()
        except:
            pass

    return text
