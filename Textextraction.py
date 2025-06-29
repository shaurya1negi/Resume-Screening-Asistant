import fitz 
import csv
import os
def pdf_content_extraction(pdf_path):
    content = {"Name":[],"Email":[],"Phone":[],"Summary":[],"Skills":[],"Professional Experience":[],"Education":[] }
    doc = fitz.open(pdf_path)
    section = None
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if line.strip():  # Only print non-empty lines
                if i == 0 :
                    content["Name"].append(line.strip())
                elif i ==1:
                    content["Email"].append(line.strip())
                elif i == 2:
                    content["Phone"].append(line.strip())
                elif line.strip() == "Summary" or section =="Summary":
                    if line.strip() == "Skills":
                        section = "Skills"
                        continue 
                    section = "Summary" #if SUmmary is reached then activate summary section
                    content["Summary"].append(line.strip())

                elif line.strip() == "Skills" or section =="Skills":
                    if line.strip() == "Professional Experience":
                        section = "Professional Experience"
                        continue
                    section = "Skills"
                    content["Skills"].append(line.strip())

                elif line.strip() == "Professional Experience" or section =="Professional Experience":
                    if line.strip() == "Education":
                        section = "Education"
                        continue
                    section = "Professional Experience"
                    content["Professional Experience"].append(line.strip())

                elif line.strip() == "Education" or section =="Education":
                    content["Education"].append(line.strip())
        # Remove all "l" entries from all list values in content present due to '.' in the pdf.
        cleaned_content = {k: [item for item in v if item != "l"] for k, v in content.items()}
    return cleaned_content

def pdf_to_csv(pdf_path, csv_path, mode='w'):
    content = pdf_content_extraction(pdf_path)
    flat_content = {k: ' '.join(v) for k, v in content.items()}
    flat_content['Filename'] = os.path.basename(pdf_path)
    with open(csv_path, mode, newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=flat_content.keys())
        if mode == 'w':
            writer.writeheader()
        writer.writerow(flat_content)

def pdf_content_to_csv(pdf_folder, csv_path):
    """
    Iterates through all PDF resumes in the folder, applies pdf_to_csv to each, and appends all data to a single CSV file.
    Assumes pdf_to_csv(pdf_path, csv_path, mode) calls pdf_content_extraction and writes to CSV.
    """
    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    for idx, pdf_file in enumerate(pdf_files):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        # For the first file, write header; for others, append without header
        mode = 'w' if idx == 0 else 'a'
        pdf_to_csv(pdf_path, csv_path, mode)
    print(f"All resumes processed and saved to {csv_path}")





