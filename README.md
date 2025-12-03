# learning-portfolio

Titanic — EDA & Data Cleaning

A small learning project demonstrating exploratory data analysis, visualization, missing-value handling, and simple feature engineering on the Titanic dataset.

## Repository layout

- `01-eda-titanic-analysis/`
	- `notebooks/01_eda_titanic.ipynb` — interactive EDA, plots, and step-by-step cleaning.
	- `data/` — place the raw CSV (`Titanic-Dataset.csv`) here. The cleaning script writes `titanic_clean.csv` to this folder.
	- `src/data_cleaning.py` — script to reproduce the cleaning steps programmatically.
- `README.md` — this file.
- `requirements.txt` — Python dependencies used in the project.

## What this project does

- Loads the Titanic CSV dataset.
- Explores distributions and missing values with visualizations.
- Engineers simple features:
	- `FamilySize` = `SibSp` + `Parch` + 1
	- `IsAlone` (1 if `FamilySize == 1`)
	- `Title` (extracted from `Name`)
	- `CabinKnown` (1 if a cabin entry exists)
- Imputes missing values:
	- `Age` filled with the median
	- `Embarked` filled with the mode
- Exports a cleaned CSV to `data/titanic_clean.csv` for downstream analysis.

## Quick start (Windows PowerShell)

1. Change to the repository root and create a virtual environment:

```powershell
cd C:\Users\Anja\learning-portfolio
python -m venv .venv
```

2. Activate the venv (PowerShell):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process  # if activation is blocked
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the cleaning script (writes `data/titanic_clean.csv`):

```powershell
python .\01-eda-titanic-analysis\src\data_cleaning.py
```

5. Open the notebook (after installing Jupyter):

```powershell
jupyter notebook
# then open 01-eda-titanic-analysis/notebooks/01_eda_titanic.ipynb in the browser
```

## Notes & recommendations

- The cleaned CSV contains imputed and engineered features but the notebook also creates an encoded copy (`df_encoded`) for inspection. If you want a model-ready file with numeric `Sex` and one-hot encoded `Title`/`Embarked`, either use the notebook's encoded cell or export an encoded CSV from `src/data_cleaning.py`.
- Consider grouping rare `Title` values into `'Other'` before one-hot encoding to reduce sparsity.
- You may improve Age imputation by using group medians (for example by `Title` or `Pclass`) instead of the global median.

## License

This is a personal learning project — add a license (e.g., MIT) if you plan to publish it publicly.

## Contact

Your name or GitHub handle (replace this line with your preferred contact).