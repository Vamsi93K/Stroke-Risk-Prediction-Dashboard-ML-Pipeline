import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote_plus

df = pd.read_csv("D:\\healthcare-dataset-stroke-data.csv")

username = "root"
password = "Store@033"
host = "localhost"
database = "healthcare_db"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}/{database}")
df.to_sql(name='patients',con=engine,if_exists='replace',index = False)

query = """
SELECT gender,SUM(stroke) AS stroke_cases
FROM patients
GROUP BY gender;
"""
df = pd.read_sql(query,con=engine)
plt.figure(figsize=(6,6))
plt.pie(df['stroke_cases'], labels=df['gender'], autopct='%1.1f%%',startangle=140,colors=['lightblue','lightgreen','salmon'])
plt.title("Stroke Cases by Gender")
plt.axis('equal')
plt.show()