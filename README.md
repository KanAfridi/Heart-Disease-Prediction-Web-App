## Heart Disease Prediction project

I have been working on this project for quite some time, and it has become one of my favorite projects. It combines multiple skills and tools I’ve learned, including Docker, GitHub Actions, Streamlit for web app development, exploratory data analysis (EDA), and using pickle files to save models and pipelines. I also implemented rigorous testing for the model and application. 

Through this project, I aimed to achieve the best possible results, and I successfully achieved an 86% accuracy for predicting heart disease. This project reflects my dedication to applying and enhancing my data science and software development skills.


### Software And Tools Requirements
1. [Github Account](https:\\github.com)
2. [Vs Code IDE](https:\\code.visualstudio.com)
3. [Git Cli](https:https://git-scm.com/downloads)
4. []

### Create New Inviroment
```
python -m venv myvenv
or
conda create -p venv python==3.7 -y
```

### 📦 Install Requirements
```
pip install -r requirements.txt
```

## 🚀 Running Streamlit App
- then i try to run streamlit alone if it's working 


## 🧪 Test the Model
- Testing the application is an essential step. To run the tests locally
```
pytest tests\test.py
```

## 🔧 GitHub Workflow
- For automation, the project includes a .github folder with a main.yaml file. This workflow will automatically:

    - *Install dependencies.*
    - *Run tests on Ubuntu (or any specified operating system).*
    - *Ensure everything works seamlessly during CI/CD processes.*

## 📂 Project Structure
**HEART-DISEASE-PREDICTION**
```
│
├── .github/
│   └── workflows/
│       └── main.yaml  # GitHub actions for CI/CD automation
│
├── src/
│   ├── __init__.py
│   └── app.py        # Streamlit application file
│
├── tests/
│   ├── __init__.py
│   └── test.py       # Test file for validating app functionality
│
├── myvenv/           # Virtual environment folder
├── df.pkl            # Serialized model
├── pipeline.pkl      # Preprocessing pipeline file
├── README.md         # This file
├── requirements.txt  # List of dependencies
└── Etc..             # Other necessary files
```

## ⚙️ What I Have Done So Far:
1. **Environment Setup:** I’ve set up both virtual and conda environments to ensure the project runs in an isolated setup.
2. **Dependencies Installation:** I’ve included all the required packages in requirements.txt for easy installation.
3. **Streamlit App:** The app.py file runs the prediction model using Streamlit. I verified that it works by testing it locally.
4. **Testing:** I created a tests/ folder to include test files, ensuring the app is working correctly before deployment. The tests are written in test.py.
5. **GitHub Workflow:** I’ve set up the CI/CD pipeline in .github/workflows/main.yaml. It automates the testing and deployment processes, ensuring the app is always tested on a fresh system.

## 🔍 Exploratory Data Analysis (EDA)

<details>
<summary>Click to expand for EDA insights</summary>

**Data Analysis and Insights**

The analysis of heart disease data reveals several key insights into the characteristics and symptoms associated with heart disease:

**Age and Heart Disease**
- Most individuals with heart disease experience chest pain and are typically over the age of 50. This indicates that heart disease is more prevalent in older populations.

**Gender Distribution**
- The percentage of males with heart disease is **90.16%**, whereas females account for **9.84%**. This highlights a significantly higher prevalence of heart disease among males.

**Maximum Heart Rate (MaxHR)**
- Individuals with heart disease tend to have a **lower maximum heart rate**, while those without heart issues generally have higher maximum heart rates.

**Resting Blood Pressure**
- People with heart disease have **slightly higher resting blood pressure** compared to those without the disease.

**Cholesterol Levels**
- Cholesterol levels are **slightly elevated** in individuals with heart disease compared to those without it.

**ST Slope**
- A **flat ST slope** is one of the most significant symptoms of heart disease. A **downsloping ST segment** is also occasionally observed.

**Resting ECG**
- While many individuals with **normal resting ECG results** still have heart disease, those with **abnormal ST-T wave (ST) results** show a higher likelihood of having heart disease. This suggests that ST abnormalities are a stronger indicator.

**MaxHR and Age**
- There is an **inverse relationship** between age and MaxHR. As age increases, MaxHR tends to decrease, indicating that younger individuals generally have higher MaxHR values.

# </details>

## 📈 Key Information

- Heart disease is more common in individuals **over 50**, especially males (**90.16%**).  
- Patients show lower MaxHR and slightly higher blood pressure and cholesterol.  
- A **flat ST slope** is a significant indicator of heart disease.  
- **Abnormal ECG** readings strongly correlate with heart disease.  

