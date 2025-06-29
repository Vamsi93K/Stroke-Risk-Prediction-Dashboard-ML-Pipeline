from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("D:\\healthcare-dataset-stroke-data.csv")

username = "root"
password = "Store@033"
host = "localhost"
database = "healthcare_db"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}/{database}")
df.to_sql(name='patients', con=engine, if_exists='replace', index=False)

query = """
SELECT gender, COUNT(*) AS total_patients, SUM(stroke) AS stroke_cases
FROM patients
GROUP BY gender;
"""
df_vis = pd.read_sql(query, con=engine)
sns.set(style="whitegrid")
sns.barplot(data = df_vis, x='gender', y='stroke_cases', hue='gender',palette='pastel')
plt.title("Strokes Cases By Gender")
plt.show()