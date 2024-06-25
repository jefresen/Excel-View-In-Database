import mysql.connector
import pandas as pd
db = mysql.connector.connect(
     host="localhost",
     user="root",
     password="12345",
     database="newschema"
)

mycursor = db.cursor()

df = pd.read_excel(r'G:\data\product.xlsx')


for i, row in df.iterrows():
     sql = "INSERT INTO product (Month, Cream ,Detergent , Moisturizer , Sanitizer, Shampoo , Soap  , Total_Units , Total_Profit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
     mycursor.execute(sql, tuple(row))
     db.commit()

def view_list():
    
     mycursor.execute("SELECT * FROM Product ")
     result = mycursor.fetchall()
     for list in result:
            print(list)
view_list()
mycursor.close()
db.close()
print("Data inserted successfully")