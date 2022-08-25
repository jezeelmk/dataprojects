import pandas as pd

df = pd.read_csv('footwear_data_v1_new_column_dropped.csv')

test_list = []
def distribution_of_sales_price():
    sales_price_bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    sales_price_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450',
                          '450-500', '500-550', '550-600']




    brand_list = df['brand'].unique()

    new_df = pd.DataFrame(columns=['brand', 'sales_price_group', 'count'])

    for brand in brand_list:

        df_brand = df[df['brand'] == brand]
        df_brand['sales_price_group'] = pd.cut(df_brand['Sales price'], bins=sales_price_bins, labels=sales_price_labels)
        sales_price_group = df_brand['sales_price_group'].value_counts(sort=False).rename_axis('Sales Price Range').reset_index(name='count')

        new_list = []
        new_list.append(brand)
        for item in sales_price_group['count']:
            new_list.append(item)


        test_list.append(new_list)

distribution_of_sales_price()
#print(test_list)

mast_df = pd.DataFrame(test_list, columns=['brand', '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500', '500-550', '550-600'])
mast_df.to_csv('distribution_of_sales_price_Across_all_brands.csv', index=False)