import camelot
import pandas as pd
import os

# List of your PDF files
pdf_files = [
    "BSD-Annual-Report-2019.pdf",
    "BSD-Annual-Report-2020-1.pdf",
    "Bank-Supervision-report-2020-21-Final.pdf",
    "Annual-Report-2022.pdf",
    "FINAL-BSD-Annual-Report-2022-23.pdf",
    "Annual-Bank-Supervision-Report-2024-3.pdf",
    "BANK-SUPERVISION-REPORT-2025.pdf"
]

# You can limit to specific pages to speed things up
# For example, pages='50-55' for the 2019 report annexes
# pages='all' extracts everything

for pdf in pdf_files:
    if os.path.exists(pdf):
        print(f"\n📄 Processing {pdf}...")
        try:
            # Extract tables using camelot (lattice works well for grid-based tables)
            tables = camelot.read_pdf(
                pdf, 
                pages='all',  # Change to '50-55' to only extract annexes
                flavor='lattice',
                strip_text='\n'
            )
            print(f"   Found {len(tables)} tables")
            
            # Save each table separately for inspection
            for i, table in enumerate(tables):
                output_name = pdf.replace('.pdf', f'_table_{i+1}.csv')
                table.df.to_csv(output_name, index=False)
            
            print(f"   ✅ Saved to {pdf.replace('.pdf', '_table_*.csv')}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    else:
        print(f"   ⚠️ File not found: {pdf}")

print("\n✅ Done! Check the CSV files in this folder.")