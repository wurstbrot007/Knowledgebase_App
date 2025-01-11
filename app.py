import streamlit as st
import PyPDF2
import openai
import os

# OpenAI API Key
os.environ["OPENAI_API_KEY"] = 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


# App-Titel
st.title("Dokumentenbasierte Frage-Antwort-App")

# Schritt 1: PDF hochladen
st.header("1. Lade ein PDF-Dokument hoch")
uploaded_file = st.file_uploader("Ziehe hier ein PDF hinein oder wähle eine Datei aus", type="pdf")

if uploaded_file:
    st.success(f"Die Datei {uploaded_file.name} wurde erfolgreich hochgeladen!")

    # PDF-Inhalt extrahieren
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    document_text = ""
    for page in pdf_reader.pages:
        document_text += page.extract_text()

    st.info("Das Dokument wurde verarbeitet. Jetzt kannst du Fragen dazu stellen!")

    # Schritt 2: Frage eingeben
    st.header("2. Frage eingeben")
    question = st.text_input("Was möchtest du über das Dokument wissen?")

    if question:
        # OpenAI API Anfrage mit Chat-Modell
        prompt = f"Beantworte die folgende Frage basierend auf diesem Text:\n\n{document_text}\n\nFrage: {question}\nAntwort:"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Du bist ein hilfsbereiter Assistent."},
                    {"role": "user", "content": prompt},
                ]
            )
            st.header("Antwort der KI")
            st.write(response['choices'][0]['message']['content'].strip())
        except Exception as e:
            st.error(f"Ein Fehler ist aufgetreten: {e}")
