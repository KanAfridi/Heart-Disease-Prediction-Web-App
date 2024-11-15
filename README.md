## Heart Disease Prediction project




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

