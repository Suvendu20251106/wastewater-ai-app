import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# --- Simulated dataset ---
data = pd.DataFrame({
    'pH': [6.5, 9.2, 7.1, 5.5],
    'BOD': [30, 100, 60, 150],
    'COD': [150, 400, 200, 500],
    'TDS': [600, 800, 650, 900],
    'TSS': [200, 300, 250, 350],
    'Usable': ['Yes', 'No', 'Yes', 'No']
})

# --- Train the model ---
le = LabelEncoder()
data['Usable_Label'] = le.fit_transform(data['Usable'])

X = data[['pH', 'BOD', 'COD', 'TDS', 'TSS']]
y = data['Usable_Label']
model = RandomForestClassifier()
model.fit(X, y)
st.write("✅ Model trained successfully.")

# --- App UI ---
st.title("Wastewater Reuse Advisor")
ph = st.slider("pH", 0.0, 14.0, 7.0)
bod = st.number_input("BOD (mg/L)", 0.0)
cod = st.number_input("COD (mg/L)", 0.0)
tds = st.number_input("TDS (mg/L)", 0.0)
tss = st.number_input("TSS (mg/L)", 0.0)

if st.button("Analyze Water"):
    input_data = np.array([[ph, bod, cod, tds, tss]])
    prediction = model.predict(input_data)[0]
    result = le.inverse_transform([prediction])[0]

    st.subheader(f"Water Usable: {result}")
