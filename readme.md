## Workflow

- config.yaml
- entity
- config/configuration.py
- - components
- pipeline
- main.py
- app.py

# How to run?

## 1. Create a conda environment after opening the repo
```bash
conda create -n books python=3.7.10 -y
```

## 2. Activate
...bash
conda activate books
...

## 3. Install the requirements
```bash
pip install -r requirements.txt
```

## 4. Run the app.py file
```bash
streamlit run app.py
```