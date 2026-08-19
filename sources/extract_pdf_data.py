import tabula
import pandas as pd
import os

# List of your PDF files (adjust names if needed)
pdf_files = [
    "BSD-Annual-Report-2019.pdf",
    "BSD-Annual-Report-2020-1.pdf",
    "Bank-Supervision-report-2020-21-Final.pdf",
    "Annual-Report-2022.pdf",
    "FINAL-BSD-Annual-Report-2022-23.pdf",
    "Annual-Bank-Supervision-Report-2024-3.pdf",
    "BANK-SUPERVISION-REPORT-2025.pdf"
]

# This will extract all tables from all pages of each PDF
# and save as CSV files for inspection.

for pdf in pdf_files:
    if os.path.exists(pdf):
        print(f"\nProcessing {pdf}...")
        try:
            # Extract all tables from all pages
            tables = tabula.read_pdf(pdf, pages='all', multiple_tables=True, lattice=True)
            print(f"Found {len(tables)} tables")
            
            # Combine into one dataframe
            if tables:
                combined = pd.concat(tables, ignore_index=True)
                output_name = pdf.replace('.pdf', '_extracted.csv')
                combined.to_csv(output_name, index=False)
                print(f"Saved to {output_name}")
            else:
                print("No tables found.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File not found: {pdf}")

print("\nDone! Check the CSV files in this folder.")