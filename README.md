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

### payments

| Endpoint                                  | Metoda | Opis                            |
|-------------------------------------------|--------|---------------------------------|
| `/payments/`                              | GET    | Lista wszystkich płatności      |
| `/payments/`                              | POST   | Tworzenie nowej płatności       |
| `/payments/{id}/`		            | GET    | Pobranie detali płatności       |
| `/payments/{id}/`		            | PUT    | Aktualizacja płatności          |


---


## 📁 Struktura projektu
AutoFix/
│
├── users/           # Rejestracja, JWT, model User
├── mechanics/       # Profil warsztatu (Mechanic)
├── services/        # Usługi warsztatu
├── payments/        # Płatności
├── manage.py
└── mechanic_booking/  # ustawienia projektu
```

# Rezerwacje

### Ustawienie godzin pracy przez mechanika
1. `GET /api/mechanic/working-hours/`  
   – pobranie wszystkich ustawionych godzin pracy  
2. `POST /api/mechanic/working-hours/`  
   – dodanie godzin pracy dla danego dnia  
3. `GET /api/mechanic/working-hours/<id>/`  
   – pobranie rekordu ustawionych godzin pracy dla danego dnia  
4. `PATCH/PUT /api/mechanic/working-hours/<id>/`  
   – aktualizacja ustawionych godzin pracy  
5. `DELETE /api/mechanic/working-hours/<id>/`  
   – usunięcie rekordu ustawionych godzin pracy dla danego dnia  

---

### Zarządzanie wizytami przez mechanika
1. `GET /api/mechanic/appointments/`  
   – pobranie listy wizyt dla danego mechanika  
2. `PATCH/PUT /api/mechanic/appointments/<id>/update-status/`  
   – aktualizacja statusu wizyty przez mechanika (np. zmiana z `pending` na `confirmed`)  

---

### Zarządzanie wizytami przez klienta
1. `GET /api/client/appointments/list/`  
   – pobranie listy wizyt przez klienta  
2. `PATCH/PUT /api/client/appointments/cancel/<id>/`  
   – anulowanie wizyty przez klienta  
3. `GET /api/client/available-timeslots/<service_id>/<appointment_date>/`  
   – pobranie dostępnych timeslotów dla wybranej usługi w danym dniu  
4. `POST /api/client/appointments/`  
   – utworzenie wizyty przez klienta (należy przesłać `service_id` oraz `date`, czyli jeden z dostępnych time slotów)  

## Uruchomienie bazy danych PostgreSQL
- Skrypt [start_postgres.sh](start_postgres.sh) uruchamia kontener Docker z bazą danych PostgreSQL z odpowiednimi credentialami.
- Skrypt [seed.py](seed.py) dodaje przykładowe dane do bazy danych.