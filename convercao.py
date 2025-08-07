import pandas as pd

def csv_to_xlsx():
    """
    Lê o covid_19_clean_complete.csv e salva como covid_19_clean_complete.xlsx
    """
    csv_path = 'covid_19_clean_complete.csv'
    xlsx_path = 'covid_19_clean_complete.xlsx'
    
    df = pd.read_csv(csv_path)
    df.to_excel(xlsx_path, index=False)
    print(f"✅ Arquivo salvo em: {xlsx_path}")

if __name__ == "__main__":
    csv_to_xlsx()