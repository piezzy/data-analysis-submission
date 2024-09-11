# Project Analisis Data

## Setup Environment

### Anaconda

1. Create a new conda environment:

   ```bash
   conda create --name main-ds python=3.9
   ```

2. Activate the environment:

   ```bash
   conda activate main-ds
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Shell/Terminal

1. Create a new project directory and navigate into it:

   ```bash
   mkdir proyek_analisis_data
   cd proyek_analisis_data
   ```

2. Install pipenv and create a virtual environment:

   ```bash
   pipenv install
   pipenv shell
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Run Streamlit App

To start the Streamlit app, run the following command:

```bash
streamlit run dashboard.py
```
