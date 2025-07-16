# 🌿 Wildlife Conservation Platform

A personal copy of the comprehensive web-based platform designed to support wildlife tracking, conservation efforts, and community engagement. Built as a team project by **Aditya** and **Anushka**, this system brings together the power of data-driven decision making and user contributions to support biodiversity conservation.

## 🧠 Motivation

The project addresses the growing need for organized and accessible tools to manage wildlife data, monitor population trends, report threats, and foster public involvement. It provides functionality for researchers, conservationists, and everyday users to collaboratively document species, habitats, and conservation activity.

## 💡 Key Features

- 🔐 **User Authentication** – Signup/login with hashed passwords and secure sessions
- 🐾 **Species Directory** – Species cards with integrated image gallery
- 📍 **Location Management** – Link species with habitats and regions via dynamic data modeling
- 📈 **Population Trend Tracking** – Year-wise updates on species population via user-submitted reports
- 📸 **Contribution System** – Users can upload field reports and images through an intuitive form
- 🤝 **Community Integration** – Join communities tied to specific regions; track regional contributions and donations
- 💰 **Donation Tracking** – Log and associate donations with users and communities
- 🔄 **Triggers and Procedures (PL/SQL)** – Smart automation:
  - Assign padded user IDs like `001`, `002`, etc.
  - Automatically link users to community tables
  - Increment/decrement counters for users/contributions/donations
  - Enforce role-based validations during contribution uploads

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Flask (Python), Jinja2 templating
- **Database**: MySQL with stored procedures and triggers
- **ORM**: SQLAlchemy
- **Security**: Flask-Login, Werkzeug password hashing
- **Version Control**: Git & GitHub

## 🧪 How to Run Locally

1. Clone the repository  
   `git clone https://github.com/yourusername/wildlife-conservation-platform.git`

2. Create a virtual environment  
   `python3 -m venv venv`

3. Activate it  
   - Unix/macOS: `source venv/bin/activate`  
   - Windows: `venv\Scripts\activate`

4. Install dependencies  
   `pip install -r requirements.txt`

5. Configure your MySQL database and update `config.py` accordingly

6. Start the app  
   `python app.py`

## 🖼️ Screenshots

- Home page with dynamic species gallery and background
- Contribution form with image upload and community dropdown
- Dashboard displaying user's reports as visual cards
- Admin newsletter and donations overview

## 🤝 Team Members

- **Aditya** – Database Schema, ER Diagram, Routes implementation and Authentication integration
- **Anushka** – UI/UX design, frontend layout and styling, integration of triggers and procedures, form validation and visual polish  

## 🌱 Future Enhancements

- Admin dashboard for contribution moderation and analytics
- Admin-generated updates and news articles for conservation developments  
- Search functionality on species and community pages  
- GIS-based mapping integration for region and habitat visualization  

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

