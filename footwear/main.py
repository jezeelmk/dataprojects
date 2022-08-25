import pandas as pd

df = pd.read_csv('footwear_data_v1_new_column_dropped.csv')


def distribution_of_brands():
    """
    Returns a dataframe with the distribution of brands in the dataset.
    """
    brands = df['brand'].value_counts().rename_axis('Brands').reset_index(name='count')

    brands.to_csv('distribution_of_brands.csv', index=False)
    return brands


distribution_of_brands()




def average_star_rating_across_brands():
    """
    Returns a dataframe with the average star rating for each brand.
    """
    brands = df['brand'].unique()
    brands_df = pd.DataFrame(columns=['brand', 'avg_star_rating'])
    for brand in brands:
        brands_df = brands_df.append({'brand': brand, 'avg_star_rating': df[df['brand'] == brand]['Star rating'].mean()},
                                     ignore_index=True)
    brands_df.to_csv('average_star_rating_across_brands.csv', index=False)
    return brands_df

average_star_rating_across_brands()

def average_number_of_reivews_across_brands():
    """
    Returns a dataframe with the average number of reviews for each brand.
    """
    brands = df['brand'].unique()
    brands_df = pd.DataFrame(columns=['brand', 'avg_num_reviews'])
    for brand in brands:
        brands_df = brands_df.append({'brand': brand, 'avg_num_reviews': df[df['brand'] == brand]['Number of reviews'].mean()},
                                     ignore_index=True)



    brands_df.to_csv('average_number_of_reviews_across_brands.csv', index=False)
    return brands_df
average_number_of_reivews_across_brands()


def distribution_of_sales_price():
    sales_price_bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
    sales_price_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450',
                          '450-500', '500-550', '550-600']

    df['sales_price_group'] = pd.cut(df['Sales price'], bins=sales_price_bins, labels=sales_price_labels)
    sales_price_group = df['sales_price_group'].value_counts().rename_axis('Sales Price Range').reset_index(
        name='count')
    sales_price_group.to_csv('distribution_of_sales_price.csv', index=False)

distribution_of_sales_price()

def distribution_of_sales_price():

    test_list = []
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

    mast_df = pd.DataFrame(test_list,
                           columns=['brand', '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350',
                                    '350-400', '400-450', '450-500', '500-550', '550-600'])
    mast_df.to_csv('distribution_of_sales_price_Across_all_brands.csv', index=False)

distribution_of_sales_price()






