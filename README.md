# Projekt Blog2

Projekt bloga umożliwia zalogowanym użytkownikom przeglądanie wszystkich postów, które mają status "published". Użytkownicy mogą również tworzyć nowe posty i edytować swoje posty z poziomu bloga, a nie panelu administracyjnego. Dodatkowo stworzony został panel logowania dla użytkowników. Aplikacja `galleries` umożliwia tworzenie galerii zdjęć i dodawanie do nich zdjęć.

# Wymagania

Python 3.8 lub nowszy
Django 5.1.4
Git

# Kroki

Wszystkie kroki wykonujemy w terminalu naszego edytora

1. Klonowanie repozytorium

git clone https://github.com/MarioDraghiMS/blog2.git
cd blog2

2. Utworzenie wirtualnego środowiska

python -m venv venv
venv\Scripts\activate

3. Instalacja potrzebnych pakietów

pip install -r requirements.txt

4. Migracje baz danych

python manage.py makemigrations
python manage.py migrate

5. Tworzenie administratora

python manage.py createsuperuser

6. Uruchamiamy serwer deweloperski

python manage.py runserver

7. Przeglądanie projektu w przeglądarce

Wklejenie linku http://127.0.0.1:8000/ w przeglądarce

Struktura projektu
/ - Strona główna do obserwowania postów i aplikacja zarzadzania postami
galleries/ - Aplikacja do zarządzania galeriami zdjęć.
blog2 - Główna konfiguracja projektu Django.


Użycie
Logowanie:

Przejdź do /accounts/login/ i zaloguj się za pomocą utworzonego superużytkownika.
Przeglądanie postów:

Przejdź do strony głównej, aby zobaczyć listę opublikowanych postów.
Tworzenie i edytowanie postów:

Zalogowani użytkownicy mogą tworzyć nowe posty i edytować swoje posty.
Tworzenie galerii i dodawanie zdjęć:

Przejdź do /galleries/, aby tworzyć nowe galerie i dodawać do nich zdjęcia.
Uwagi