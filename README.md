# Student Management System (Streamlit + OOP)

A small, modular Student Management System implemented with Python OOP and Streamlit for UI.

Structure
- `models/` — domain models (e.g., `Student`).
- `services/` — logic for storage and student management (`StorageService`, `StudentManager`).
- `ui/` — Streamlit UI pages/components (add, update, delete, list, search, fees & attendance).
- `data/students.json` — sample data file (created for quick demo).
- `app.py` — Streamlit entrypoint.

Setup
1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

Run
```powershell
# from workspace root
python -m streamlit run student_management_system/app.py
```

Notes
- If you're on Windows and can't run `Activate.ps1` due to execution policy, either run Streamlit with `python -m streamlit run ...` or change policy as needed.
- The sample data file `data/students.json` is used by `StorageService` by default. Edit or replace it to pre-populate records.
- I can add unit tests, more validation, or packaging if you want.
# 🎓 Student Management System (Streamlit + Python OOP)

A complete student management system built using:

- Python OOP
- Streamlit UI
- JSON persistent storage
- Modular folder architecture

---

## 📁 Project Structure

See full structure in the code section.

---

## 🚀 Run the Application

1. Install dependencies:

```bash
pip install streamlit pandas
