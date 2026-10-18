# Login Brute-Force Protector

A Theory of Computation project demonstrating how a **Deterministic Finite Automaton (DFA)** can control login attempts and transition to a locked state after repeated authentication failures.

## Overview

The application provides a simple login interface backed by a DFA. Each authentication attempt triggers a state transition based on the supplied credentials and the current state of the automaton.

### Features

- Login form with username and password fields.
- DFA-based authentication state management.
- Tracking of consecutive failed login attempts.
- Locked state after the configured failure limit is reached.
- Reset functionality to return the automaton to its initial state.
- Web interface built with HTML and CSS using Flask.

## DFA States

| State | Description |
|---|---|
| `START` | Initial state, ready for authentication. |
| `ONE_FAIL` | One consecutive login attempt has failed. |
| `TWO_FAIL` | Two consecutive attempts have failed, if represented separately in the implementation. |
| `LOCKED` | Authentication is blocked after the configured failure limit. |
| `SUCCESS` | Credentials have been accepted. |

The exact state transitions and failure limit are determined by the implementation in `dfa.py`. Successful authentication and reset behavior depend on the application's transition logic.

## Technology Stack

- **Language:** Python
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Core concept:** Deterministic Finite Automata (DFA)

## Project Structure

```text
Login_Brut_Force_Protector/
├── app.py
├── dfa.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Prerequisites

- Python 3 installed
- Git (optional, for cloning the repository)

## Run Locally on Windows

### 1. Get the project

Clone the repository or download its source code, then open PowerShell in the project directory.

```powershell
git clone https://github.com/Richa-dev01/Login_Brut_Force_Protector.git
cd Login_Brut_Force_Protector
```

If you already have the project locally, open PowerShell in that existing directory instead.

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Start the application

```powershell
.\.venv\Scripts\python.exe app.py
```

### 5. Open the application

Visit:

http://127.0.0.1:5000

Stop the development server with `Ctrl + C`.

## Demo Credentials

If using the default local configuration, the demo credentials are:

- **Username:** `admin`
- **Password:** `admin123`

These credentials are for educational demonstration only. Use the credentials configured in `app.py` if they have been changed.

## Limitations

This is an educational demonstration of DFA-based authentication, not a production-ready authentication service. Depending on the implementation, state may be stored only in application memory and may be shared between users. Production systems require per-user or per-session tracking, secure password storage, appropriate rate limiting, and server-side access controls.

## Learning Objectives

- Understand deterministic finite automata.
- Model authentication as a finite-state system.
- Implement state transitions in Python.
- Connect theoretical state-machine concepts to a web application.
- Observe how repeated failures affect the system's state.

## License

No license has been specified. Contact the repository owner before reusing or redistributing the project.