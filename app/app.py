import streamlit as st
import pandas as pd
import joblib
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Load model and encoder
model_path = os.path.join(os.path.dirname(__file__), '..', 'mood_classifier.pkl')
encoder_path = os.path.join(os.path.dirname(__file__), '..', 'label_encoder.pkl')

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

# Streamlit app title
st.title('Spotify Mood Classifier')
st.markdown("Upload a dataset of songs and predict their mood using audio features.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type = ['csv'])

# Load default data if none uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv('data/tracks.csv')
    st.markdown("*Using default sample dataset from `/data/tracks.csv`*")

# Display raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df.head())

# Check required columns
required_clos = ['valence', 'energy', 'danceability', 'tempo', 'acousticness', 'speechiness']
if not all(col in df.columns for col in required_clos):
    st.error(f"CSV must contain columns: {', '.join(required_cols)}")
    st.stop()

# Prediction
X = df[required_clos]
df['predicted_mood'] = label_encoder.inverse_transform(model.predict(X))

# Show mood predictions
st.subheader("Predicted Moods")
#st.dataframe(df[['name', 'artists', 'predicted__mood']].head(20))
columns_to_display = ['predicted_mood']
for col in ['name', 'artists']:
    if col in df.columns:
        columns_to_display.insert(0, col)
st.dataframe(df[columns_to_display].head(20))

# Mood distribution plot
st.subheader('Mood Distribution')

mood_counts = df['predicted_mood'].value_counts().reset_index()
mood_counts.columns = ['Mood', 'Count']

fig, ax = plt.subplots()
sns.barplot(x = 'Count', y = 'Mood', data = mood_counts, palette = 'coolwarm', ax= ax)
st.pyplot(fig)

# Download button
csv = df.to_csv(index = False).encode('utf-8')
st.download_button("📥 Download Predictions as CSV", csv, "mood_predictions.csv", "text/csv")
