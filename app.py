import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Simulate training data
data = pd.DataFrame({
    'pH': [6.5, 9.2, 7.1, 5.5],
    'BOD': [30, 100, 60, 150],
    'COD': [150, 400, 200, 500],
    'TDS': [600, 800, 650, 900],
    'TSS': [200, 300, 250, 350],
    'Usable': ['Yes', 'No', 'Yes', 'No']
})

le = LabelEncoder()
data['Usable_Label'] = le.fit_transform(data['Usable'])

X = data[['pH', 'BOD', 'COD', 'TDS', 'TSS']]
y = data['Usable_Label']
model = RandomForestClassifier()
model.fit(X, y)

# Now use model.predict(...) as usual
