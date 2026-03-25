# CSW2 Blog Application

A full-featured blog web application built with Python and Django, designed to demonstrate modern Django development practices.

## New Features & Highlights

This project has been recently updated to include several advanced Django concepts:

- **Class-Based Views (CBVs):** Transitioned from function-based views to robust CBVs (`ListView`, `DetailView`, `CreateView`) for handling blog post listing, details, and creation efficiently.
- **Advanced Authentication:** 
  - Complete Login, Logout, and Registration system using Django's built-in Auth Views.
  - Route protection using `LoginRequiredMixin` to ensure only authenticated users can create new posts (`/post/new/`).
- **Django Signals:** Implemented `@receiver(post_save, sender=User)` to automatically generate and save a `Profile` instance whenever a new `User` is registered, keeping user data synchronized.
- **Media & Profile Pictures:** 
  - Full support for user-uploaded media files.
  - Integrated with the `Pillow` library to handle custom profile pictures on user profile pages.
- **Enhanced UI/UX:** 
  - Forms are styled uniformly using **Django Crispy Forms** with the **Bootstrap 5** template pack.
  - Custom Navigation Bar (Navbar) and refined CSS layouts for a responsive, modern feeling.

## Core Functionality

- **User Profiles:** Personalized user profiles displaying the user's information and custom profile picture.
- **Blog Posts:** Users can read posts from others or create their own.
- **Post Details:** Each post dynamically routes to a detailed view (`post/<int:pk>/`), displaying the title, content, author, and timestamp.

## Tech Stack

- **Backend:** Python, Django 5.2
- **Database:** SQLite3 (default)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Image Processing:** Pillow
- **Forms:** Django Crispy Forms (bootstrap5)

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aryan1196/CSW2_blogapp.git
   cd CSW2_blogapp
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv djangoEnv
   # On Windows:
   djangoEnv\Scripts\activate
   # On macOS/Linux:
   source djangoEnv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   cd django_project1
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://123.0.0.1:8000/`.

## Application Structure

- `django_project1/`: Main Django project configuration directory (Settings, Core URLs).
- `blog/`: The core blog app handling CBVs (`ListView`, `DetailView`, `CreateView`) and routing for content.
- `users/`: The user management app handling authentication, signals for automatic profile creation, and profile views.
- `media/`: Directory where uploaded user profile pictures and files are stored.

## License

This project is licensed under the MIT License.
