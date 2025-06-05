# 🎰 Lotto Number Generator

A full-stack web application that generates random lottery numbers, stores them in a database, and provides real-time statistics through an interactive UI.

---

## 64294(Fatih Sanlı)-66799(Emir Akyer)-64293(Sarkhan Rahimov)-66604(Ali Valiyev)-66715(Shahin Feyzizade)
---

## 📌 Project Objective

The application enables users to:
- Generate a set of 6 random lottery numbers.
- Store each draw with a timestamp.
- View statistics such as total draws, draws in the last 24 hours, and most frequently drawn numbers.

---

## 🧱 Architecture Overview

**Pattern:** Model-View-Controller (MVC)

- **Model:** `LottoDraw` stores the numbers (as a JSON list) and creation time.
- **View:** Django API views + Vue components.
- **Controller:** Django `urls.py` and Vue Router handle navigation and logic.

---

## 🛠️ Technologies

### 🔧 Backend
- Python 3
- Django 5.0
- Django REST Framework
- SQLite (PostgreSQL compatible)

### 💻 Frontend
- Vue 3
- Vuetify 3
- TypeScript
- Vite

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd lottonumbergenerator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Django Migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Django Backend

```bash
python manage.py runserver
```

The backend will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Running the Frontend

### 1. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 2. Start the Frontend Development Server

```bash
npm start
```

The frontend will typically be available at [http://localhost:5173/](http://localhost:5173/).

---

## API Endpoints

- `GET /api/generate_numbers/` — Generate random lotto numbers and save to DB
- `GET /api/stats/` — Get statistics (last 24h draws, total draws, most common number)


---

![44](https://github.com/user-attachments/assets/60c0997e-c5f4-4855-83ef-1de78e7b992b)
![33](https://github.com/user-attachments/assets/38672648-3548-47de-bff7-f04d74bed8f5)
![22](https://github.com/user-attachments/assets/76eddabb-212d-4141-9a26-18aa47fc97a9)
![11](https://github.com/user-attachments/assets/28c885af-8b80-4b28-bee5-7ef0766f41bf)


https://github.com/user-attachments/assets/07b531d9-e1fe-465c-97ae-2b12db336ebc



