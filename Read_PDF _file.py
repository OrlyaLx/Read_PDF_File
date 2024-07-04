import PyPDF2
import os
import re

# Funcția pentru a extrage textul din PDF
def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Fișierul {pdf_path} nu există.")
        return None

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Funcția pentru a analiza și filtra textul
def filter_and_extract_keyword_data(text, keyword):
    pattern = re.compile(rf'{keyword}\s*(\S+)')
    matches = pattern.findall(text)
    return matches

# Funcția pentru a extrage textul dintre două cuvinte cheie
def extract_text_between_keywords(text, start_keyword, end_keyword):
    pattern = re.compile(rf'{start_keyword}(.*?){end_keyword}', re.DOTALL)
    match = pattern.search(text)
    return match.group(1).strip() if match else None

# Funcția pentru a extrage data-țintă
def extract_target_date(text, target_keyword):
    pattern = re.compile(rf'{target_keyword}\s*([\d]{{2}}.[\d]{{2}}.[\d]{{4}})')
    match = pattern.search(text)
    return match.group(1) if match else None

# Funcția pentru a extrage textul între "Depozitul nr." și "Defecțiune nr."
def extract_text_between_depositions(text, start_keyword, end_keyword):
    pattern = re.compile(rf'{start_keyword}(.*?){end_keyword}', re.DOTALL)
    match = pattern.search(text)
    return match.group(1).strip() if match else None

# Path-ul către fișierul PDF (înlocuiește cu calea corectă)
pdf_path = 'C:/Users/Orlando/Desktop/Test3.pdf'  # Exemplu pentru Windows
# pdf_path = '/home/username/Documents/document.pdf'  # Exemplu pentru macOS/Linux

# Cuvântul cheie de căutat
keyword = "Comandă nu.:"
start_keyword = "Informații despre comandă"
end_keyword = "Notă de comandă"
target_date_keyword = "Data-țintă"
deposition_start_keyword = "Depozitul nr."
deposition_end_keyword = "Defecțiune nr."
deposition_start_keyword_1 = "Adresă de livrare"
deposition_end_keyword_1 = "Depozitul nr."

# Extrage textul din PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Filtrează textul și afișează datele găsite
if extracted_text:
    # Extrage și afișează liniile care conțin keyword-ul
    filtered_data = filter_and_extract_keyword_data(extracted_text, keyword)
    for data in filtered_data:
        print(f"{keyword} {data}")
    
    # Extrage și afișează textul dintre cele două cuvinte cheie
    extracted_section = extract_text_between_keywords(extracted_text, start_keyword, end_keyword)
    if extracted_section:
        print(f"\nInformații despre comandă : {extracted_section}")     
    else:
        print("\nNu s-a găsit nicio secțiune între cuvintele cheie specificate.")
    
    # Extrage și afișează data-țintă
    target_date = extract_target_date(extracted_text, target_date_keyword)
    if target_date:
        print(f"\nData-țintă: {target_date}")
    else:
        print("\nData-țintă nu a fost găsită.")
    
    # Extrage și afișează textul între "Depozitul nr." și "Defecțiune nr."
    extracted_deposition_section = extract_text_between_depositions(extracted_text, deposition_start_keyword, deposition_end_keyword)
    if extracted_deposition_section:
        print(f"\nNumar Magazin: {extracted_deposition_section}")
        
    else:
        print("\nNu s-a găsit nicio secțiune între 'Depozitul nr.' și 'Defecțiune nr.'.")
        
    # Extrage și afișează textul între "Adresă de livrare" și "Depozitul nr."
    extracted_deposition_section_1 = extract_text_between_depositions(extracted_text, deposition_start_keyword_1, deposition_end_keyword_1)
    if extracted_deposition_section:
        print(f"\nAdresă de livrare: {extracted_deposition_section_1}")
        
    else:
        print("\nNu s-a găsit nicio secțiune între 'Depozitul nr.' și 'Defecțiune nr.'.")

