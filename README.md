# 🔧 AutoFix API – Backend 

## ⚙️ Jak uruchomić projekt lokalnie

```bash
git clone <adres_repozytorium>
cd AutoFix
python -m venv env
source env/bin/activate
pip install -r requirements.txt

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'autofix',
        'USER': 'autofix_user',
        'PASSWORD': 'autofix_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Inicjalizacja bazy danych:
python manage.py makemigrations
python manage.py migrate

## 🔧 Endpointy API

### 🔹 Mechanik (wymaga autoryzacji)

| Endpoint                            | Metoda | Opis                               |
|-------------------------------------|--------|------------------------------------|
| `/api/mechanic/me/`                 | GET    | Pobierz swój profil warsztatu      |
| `/api/mechanic/me/`                 | PUT    | Uzupełnij/edytuj dane warsztatu    |
| `/api/mechanic/services/`           | GET    | Lista własnych usług               |
| `/api/mechanic/services/`           | POST   | Dodaj nową usługę                  |
| `/api/mechanic/services/{id}/`      | PUT    | Edytuj usługę                      |
| `/api/mechanic/services/{id}/`      | DELETE | Usuń usługę                        |

---

### 🌍 Klient (dostęp publiczny)

| Endpoint                                  | Metoda | Opis                            |
|-------------------------------------------|--------|---------------------------------|
| `/api/services/`                          | GET    | Lista wszystkich usług          |
| `/api/services/?city=Warszawa`            | GET    | Filtrowanie po mieście          |
| `/api/services/?mechanic_id=5`            | GET    | Filtrowanie po mechaniku        |

---

## 📁 Struktura projektu
AutoFix/
│
├── users/           # Rejestracja, JWT, model User
├── mechanics/       # Profil warsztatu (Mechanic)
├── services/        # Usługi warsztatu
├── manage.py
└── mechanic_booking/  # ustawienia projektu
