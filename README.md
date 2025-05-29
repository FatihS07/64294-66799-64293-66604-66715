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



