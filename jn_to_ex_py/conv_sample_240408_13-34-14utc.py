#!/usr/bin/env python
# coding: utf-8

# # Notebooksample 0.0.1

# ## Codesample 1  Database

# In[ ]:


import pandas as pd
# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 28, 24],
    'Salary': [50000, 60000, 45000, 55000, 52000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
df


# # Codesample 2 = Maths 

# In[ ]:


import matplotlib.pyplot as plt

# Calculate average age and salary
average_age = df['Age'].mean()
average_salary = df['Salary'].mean()

# Print the calculated values
print("Average Age:", average_age)
print("Average Salary:", average_salary)

# Create a bar plot of salaries
plt.bar(df['Name'], df['Salary'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary Distribution')
plt.show()


# ## Markdownsample = Integrating a Picture: 

# ![Titanic](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/1024px-RMS_Titanic_3.jpg)
# 
# Image Source: [Wikipedia](https://en.wikipedia.org/wiki/RMS_Titanic)

# In[ ]:


# Python-Converter 
"""
from nbconvert import PythonExporter
import nbformat
from datetime import datetime, timezone # erstellen von timestamps 

# import os # erstellen fortlaufender nummern = counter 

# Zähler für die Nummerierung bei import os 
# counter = 1 

# Generierung des Timestamps im Format "JJMMTT.hh-mm-ss"
utc_timestamp = datetime.now(timezone.utc).strftime("%y%m%d_%H-%M-%S")

# Laden des Notebooks
with open("notebooksample.ipynb", "r") as f:
    nb = nbformat.read(f, as_version=4)

# Erstellen des Python Exporters
pe = PythonExporter()

# Speichern der konvertierten Python-Datei mit dem Timestamp im Dateinamen
file_name = f'converted_sample_{utc_timestamp}.py'
with open(file_name, 'w') as f:
    (body, resources) = pe.from_notebook_node(nb)
    f.write(body)
"""
"""# Konvertieren des Notebooks in eine Python-Datei mit fortlaufender Nummerierung
while os.path.exists(f"converted_sample{counter}.py"):
  counter += 1  

# Speichern der konvertierten Python-Datei
with open(f"converted_sample{counter}.py", "w") as f:
    (body, resources) = pe.from_notebook_node(nb)
    f.write(body)"""


# In[ ]:


# HTML-Converter

"""from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
import nbformat
from numpy import nbytes

# Erstellen des Preprocessors
ep = ExecutePreprocessor(timeout=-1)

# Ausführen des Notebooks
ep.preprocess(nbformat, {'metadata': {'path': './'}})

# Konvertieren des Notebooks in HTML
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(nbytes)

# Speichern der konvertierten Datei
with open('converted_sample.html', 'w') as f:
    f.write(body)"""

