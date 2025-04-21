# 🎵 Spotify Mood Classifier 🎧

A machine learning-powered app that classifies the mood of Spotify tracks based on their audio features. Explore the dataset, enjoy interactive visualizations, and try out the mood prediction live through a Streamlit interface!

---

## 📂 Project Structure

spotify-mood-classifier/ 
├── app/ 
│ └── app.py 
├── data/ 
│ └── tracks.csv 
├── notebooks/ 
│ └── eda.ipynb 
├── mood_classifier.pkl 
├── label_encoder.pkl 
├── requirements.txt 
├── README.md 
└── .gitignore

---

## 🧠 Features

- 🎼 **EDA**: Understand track distributions with features like danceability, energy, tempo, etc.
- 📈 **Visualizations**: Bubble plots, trend charts, and bar graphs using Seaborn & Matplotlib.
- 🤖 **Mood Classifier**: Predict moods like *Happy*, *Sad*, *Energetic*, and more based on track features.
- 💻 **Streamlit App**: User-friendly web interface for mood prediction.

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aditi14699/spotify-mood-classifier.git
   cd spotify-mood-classifier

2. **Create & Activate Virtual Environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate    # On Windows

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the Streamlit App**
    ```bash
    cd app
    streamlit run app.py

---

📊 Dataset
- Source: Kaggle - Spotify Audio Features ('https://www.kaggle.com/datasets/tomigelo/spotify-audio-features')
- Contents: Audio features of tracks including acousticness, danceability, energy, liveness, tempo, etc.

---

📌 Tech Stack
-Languages: Python
-Libraries: Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Streamlit, Joblib
-Model: Classifier trained on mood-labeled data

---

✨ Future Improvements
-Add more mood categories
-Train using larger and more recent datasets
-Enable audio preview for each track
-Deploy publicly on Streamlit Cloud

---

🙌 Acknowledgements
Thanks to Spotify, Kaggle contributors, and the open-source ML community for the resources and inspiration.

---

📬 Contact
-Creator: Aditi   
-LinkedIn: https://www.linkedin.com/in/aditi-patil-52992115b/ 