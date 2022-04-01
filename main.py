# Leer archivos txt con pandas usando read_csv y exportar a excel y csv

# Importar pandas
import pandas as pd

# Leer el archivo de texto en pandas Dataframe y crear encabezados
print("Leyendo archivo")
df = pd.read_csv("./files/example.txt", sep="\t", header=None,
                 names=["Name", "Team", "Number", "Position", "Age", "Height", "Weight", "College", "Salary"])
# Exportar excel
print("Generando excel")
df.to_excel("./files/export.xlsx")
# Exportar csv
print("Generando csv")
df.to_csv("./files/export.csv")
# Exportar excel sin index
print("Genernado excel sin index")
df.to_excel("./files/export-without-index.xlsx", index=False)