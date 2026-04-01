Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/khush/Downloads/customer beaviour project/customer_shopping.py
>>> 
= RESTART: C:/Users/khush/Downloads/customer beaviour project/customer_shopping.py
>>> 
= RESTART: C:/Users/khush/Downloads/customer beaviour project/customer_shopping.py
>>> 
>>> df = pd.read_csv('customer_shopping_behavior.csv')
>>> df.head()
   Customer ID  Age  ... Payment Method Frequency of Purchases
0            1   55  ...          Venmo            Fortnightly
1            2   19  ...           Cash            Fortnightly
2            3   50  ...    Credit Card                 Weekly
3            4   21  ...         PayPal                 Weekly
4            5   45  ...         PayPal               Annually

[5 rows x 18 columns]
>>> 
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3900 entries, 0 to 3899
Data columns (total 18 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   Customer ID             3900 non-null   int64  
 1   Age                     3900 non-null   int64  
 2   Gender                  3900 non-null   object 
 3   Item Purchased          3900 non-null   object 
 4   Category                3900 non-null   object 
 5   Purchase Amount (USD)   3900 non-null   int64  
 6   Location                3900 non-null   object 
 7   Size                    3900 non-null   object 
 8   Color                   3900 non-null   object 
 9   Season                  3900 non-null   object 
 10  Review Rating           3863 non-null   float64
 11  Subscription Status     3900 non-null   object 
 12  Shipping Type           3900 non-null   object 
 13  Discount Applied        3900 non-null   object 
 14  Promo Code Used         3900 non-null   object 
 15  Previous Purchases      3900 non-null   int64  
 16  Payment Method          3900 non-null   object 
 17  Frequency of Purchases  3900 non-null   object 
dtypes: float64(1), int64(4), object(13)
memory usage: 548.6+ KB

df.describe(include = 'all')
        Customer ID          Age  ... Payment Method Frequency of Purchases
count   3900.000000  3900.000000  ...           3900                   3900
unique          NaN          NaN  ...              6                      7
top             NaN          NaN  ...         PayPal         Every 3 Months
freq            NaN          NaN  ...            677                    584
mean    1950.500000    44.068462  ...            NaN                    NaN
std     1125.977353    15.207589  ...            NaN                    NaN
min        1.000000    18.000000  ...            NaN                    NaN
25%      975.750000    31.000000  ...            NaN                    NaN
50%     1950.500000    44.000000  ...            NaN                    NaN
75%     2925.250000    57.000000  ...            NaN                    NaN
max     3900.000000    70.000000  ...            NaN                    NaN

[11 rows x 18 columns]

df.isnull().sum()
Customer ID                0
Age                        0
Gender                     0
Item Purchased             0
Category                   0
Purchase Amount (USD)      0
Location                   0
Size                       0
Color                      0
Season                     0
Review Rating             37
Subscription Status        0
Shipping Type              0
Discount Applied           0
Promo Code Used            0
Previous Purchases         0
Payment Method             0
Frequency of Purchases     0
dtype: int64

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
df.isnull().sum()
Customer ID               0
Age                       0
Gender                    0
Item Purchased            0
Category                  0
Purchase Amount (USD)     0
Location                  0
Size                      0
Color                     0
Season                    0
Review Rating             0
Subscription Status       0
Shipping Type             0
Discount Applied          0
Promo Code Used           0
Previous Purchases        0
Payment Method            0
Frequency of Purchases    0
dtype: int64

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
SyntaxError: multiple statements found while compiling a single statement

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df.columns
Index(['customer_id', 'age', 'gender', 'item_purchased', 'category',
       'purchase_amount_(usd)', 'location', 'size', 'color', 'season',
       'review_rating', 'subscription_status', 'shipping_type',
       'discount_applied', 'promo_code_used', 'previous_purchases',
       'payment_method', 'frequency_of_purchases'],
      dtype='object')

df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
df.columns
Index(['customer_id', 'age', 'gender', 'item_purchased', 'category',
       'purchase_amount', 'location', 'size', 'color', 'season',
       'review_rating', 'subscription_status', 'shipping_type',
       'discount_applied', 'promo_code_used', 'previous_purchases',
       'payment_method', 'frequency_of_purchases'],
      dtype='object')

#create a column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q = 4, labels = labels)
df[['age', 'age_group']].head(10)
   age    age_group
0   55  Middle-aged
1   19  Young Adult
2   50  Middle-aged
3   21  Young Adult
4   45  Middle-aged
5   46  Middle-aged
6   63       Senior
7   27  Young Adult
8   26  Young Adult
9   57  Middle-aged

#create column purchase_frequency_days

frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)
   purchase_frequency_days frequency_of_purchases
0                       14            Fortnightly
1                       14            Fortnightly
2                        7                 Weekly
3                        7                 Weekly
4                      365               Annually
5                        7                 Weekly
6                       90              Quarterly
7                        7                 Weekly
8                      365               Annually
9                       90              Quarterly

df[['discount_applied', 'promo_code_used']].head(10)
  discount_applied promo_code_used
0              Yes             Yes
1              Yes             Yes
2              Yes             Yes
3              Yes             Yes
4              Yes             Yes
5              Yes             Yes
6              Yes             Yes
7              Yes             Yes
8              Yes             Yes
9              Yes             Yes

(df['discount_applied'] == df['promo_code_used']).all()
np.True_

df = df.drop('promo_code_used', axis = 1)
df.columns
Index(['customer_id', 'age', 'gender', 'item_purchased', 'category',
       'purchase_amount', 'location', 'size', 'color', 'season',
       'review_rating', 'subscription_status', 'shipping_type',
       'discount_applied', 'previous_purchases', 'payment_method',
       'frequency_of_purchases', 'age_group', 'purchase_frequency_days'],
      dtype='object')

pip install psycopg2-binary sqlalchemy
SyntaxError: invalid syntax
!pip install psycopg2-binary sqlalchemy
SyntaxError: invalid syntax
%pip install psycopg2-binary sqlalchemy
SyntaxError: invalid syntax
pip install psycopg2-binary
SyntaxError: invalid syntax
import psycopg2
import sqlalchemy
print("Libraries imported successfully!")
Libraries imported successfully!


from sqlalchemy import create_engine

#Step1: Connect to PostgreSQL
#Replace placeholder with your actual details
username = "postgres"   #default user
password = "wowwow"
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

#Step2: Load Dataframe into PostgreSQL
table name = "customer"
SyntaxError: invalid syntax
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)
900
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
Data successfully loaded into table 'customer' in database 'customer_behavior'.
