🏥 Smart Hospital Management System

A full-stack Django-based healthcare management system where patients, doctors, and admins interact using a clean Bootstrap-powered UI.

🚀 Features
👨‍⚕️ Doctor Module

Doctor signup & login

Manage profile (specialization, experience, timings, room number)

Add availability slots

View patient appointments

Update appointment status (Pending → Confirmed → Completed → Cancelled)

Add medical history for patients

🧑‍🧑‍🧒 Patient Module

Patient signup & login

Update personal profile

Book appointments

View upcoming appointments

View medical history added by doctor

🛠 Admin Panel

Admin login

Manage doctors

Manage patients

Manage appointments

View system statistics

🏗 Tech Stack

Backend: Django 5

Frontend: HTML, CSS, Bootstrap 5

Database: SQLite (default)

Authentication: Django Auth (User Model + Roles)

📂 Project Structure (Short)
hospital_project/
│── accounts/        # Login, signup, admin panel
│── doctors/         # Doctor dashboard, slots, appointments
│── patients/        # Patient dashboard, booking
│── appointments/    # Appointment model & logic
│── static/          # CSS, JS, Images
│── templates/       # Base + Shared templates
│── manage.py

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

3️⃣ Create admin
python manage.py createsuperuser

4️⃣ Start server
python manage.py runserver

5️⃣ Open in browser
http://127.0.0.1:8000/

🔐 Login Roles

Admin: Access complete system

Doctor: Manage profile, appointments, medical history

Patient: Book appointments, view history
