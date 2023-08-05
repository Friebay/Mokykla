import os
import shutil
import zipfile
from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_path, output_path, max_size_mb):
    # Create a temporary folder to store the compressed PDFs
    temp_folder = os.path.join(os.path.dirname(output_path), 'temp')
    os.makedirs(temp_folder, exist_ok=True)

    # Compress each PDF file in the input folder
    for filename in os.listdir(input_path):
        if filename.endswith('.pdf'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(temp_folder, filename)

            # Open the original PDF file
            pdf_reader = PdfReader(input_file)

            # Create a new PDF file with compressed content
            pdf_writer = PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Write the compressed content to the new PDF file
            with open(output_file, 'wb') as pdf_out:
                pdf_writer.write(pdf_out)

    # Create a ZIP file containing the compressed PDFs
    with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_folder):
            for file in files:
                zipf.write(os.path.join(root, file), file)

    # Clean up temporary folder
    shutil.rmtree(temp_folder)

if __name__ == '__main__':
    input_folder = r'C:\Users\zabit\Documents\GitHub\Mokykla\Istorija'
    output_zip_file = r'C:\Users\zabit\Documents\compressed_pdfs.zip'
    max_size_mb = 50

    compress_pdf(input_folder, output_zip_file, max_size_mb)
