# Login_Brut_Force_Protector
(Theory of computation project) The user with wrong userid and password can not enter and would be left with two attempts if both the attempt fails then it goes to lock state

## Run locally on Windows

Open PowerShell in this project folder and run:

```powershell
cd "C:\Users\prasa\OneDrive\Desktop\TOC_project\Login_Brut_Force_Protector"
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

If PowerShell blocks activation, run the project without activating the environment:

```powershell
cd "C:\Users\prasa\OneDrive\Desktop\TOC_project\Login_Brut_Force_Protector"
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

The login credentials currently configured for the demo are:

- Username: `admin`
- Password: `admin123`
