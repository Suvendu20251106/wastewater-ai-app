import streamlit as st
import joblib
import numpy as np

# Load model and encoders
model = joblib.load('usable_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')
treatment_rules = joblib.load('treatment_rules.pkl')

st.title("Wastewater Reuse Advisor for Pulp & Paper Industry")

# User input
ph = st.slider("pH", 0.0, 14.0, 7.0)
bod = st.number_input("BOD (mg/L)", 0.0)
cod = st.number_input("COD (mg/L)", 0.0)
tds = st.number_input("TDS (mg/L)", 0.0)
tss = st.number_input("TSS (mg/L)", 0.0)

if st.button("Analyze Water"):
    input_data = np.array([[ph, bod, cod, tds, tss]])
    usable_prediction = model.predict(input_data)[0]
    usable_text = label_encoder.inverse_transform([usable_prediction])[0]

    # Treatment suggestion
    treatment = []
    if ph < 6.5:
        treatment.append(treatment_rules['acidic'])
    elif ph > 8.5:
        treatment.append(treatment_rules['alkaline'])
    if bod > 50:
        treatment.append(treatment_rules['high_BOD'])
    if cod > 250:
        treatment.append(treatment_rules['high_COD'])
    if not treatment:
        treatment.append(treatment_rules['normal'])

    st.subheader(f"Water Usable: {usable_text}")
    st.write("Recommended Treatment:", ", ".join(treatment))
