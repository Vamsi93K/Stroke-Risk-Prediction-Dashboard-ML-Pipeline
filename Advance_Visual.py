#Heatmap visualization
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
df = pd.read_csv("D:\\healthcare-dataset-stroke-data.csv")


username = "root"
password = "Store@033"
host = "localhost"
database = "healthcare_db"
encoded_password = quote_plus(password)

# Create the connection string
engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@{host}/{database}")
df.to_sql(name='patients', con=engine, if_exists='replace', index=False)
print("✅ Data successfully loaded into MySQL!")

df = pd.read_sql("SELECT * FROM patients", con=engine)

# Compute correlation matrix
corr = df.corr(numeric_only=True)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap of Patient Features")
plt.tight_layout()
plt.show()