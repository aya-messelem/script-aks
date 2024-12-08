import pandas as pd

file_path = r'c:\Users\ayame\Downloads\Log intern - Analyst case study.xlsx'  
output_file_path = r'c:\Users\ayame\OneDrive\Desktop\AKS solution\output.xlsx'  # Path to save the output Excel file

# Load the relevant sheets
excel_data = pd.ExcelFile(file_path)
data_brands = excel_data.parse('Data brands')
data_orders = excel_data.parse('Data orders')

# Filter FF_synced brands from Data brands
ff_synced_brands = data_brands[data_brands['fg_ff_sync*'] == True]['uuid_brand']

# Filter orders for FF_synced brands from Data orders
filtered_orders = data_orders[data_orders['uuid_brand'].isin(ff_synced_brands)]

# Group orders by uuid_brand and calculate the number of orders per brand
order_counts = filtered_orders.groupby(['uuid_brand', 'Order reference']).size().reset_index(name='number_of_orders')

# Rename columns for clarity
order_counts = order_counts.rename(columns={
    'uuid_brand': 'uuid_brand',
    'number_of_orders': 'number of orders per reference',
    'Order reference': 'order reference'
})

# Write the resulting DataFrame to an Excel file
order_counts.to_excel(output_file_path, index=False)

print(f"Output successfully written to {output_file_path}")

