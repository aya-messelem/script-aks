import pandas as pd

file_path = r"c:\Users\ayame\OneDrive\Desktop\aks case\Log intern - Analyst case study.xlsx"

df_orders = pd.read_excel(file_path, sheet_name='Data orders')  
df_sync = pd.read_excel(file_path, sheet_name='Data brands')    

print("Colonnes dans df_orders :", df_orders.columns)
print("Colonnes dans df_sync :", df_sync.columns)

df_merged = df_orders.merge(df_sync, on='uuid_brand', how='inner', suffixes=('_orders', '_brands'))
print("Fusion réussie. Colonnes dans df_merged :", df_merged.columns)


if 'fg_ff_sync*_orders' in df_merged.columns:
    ff_synced_brands = df_merged[df_merged['fg_ff_sync*_orders'].notna()]
    print(f"{len(ff_synced_brands)} marques synchronisées FF trouvées.")
    

