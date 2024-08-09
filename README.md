# Student and Course Registration System

Welcome to the Student and Course Registration System! This is a Django-based web application that allows students to register for courses and manage their information.

## Features

- **Student Registration**: Allows students to create and manage their profiles.
- **Course Registration**: Enables students to register for available courses.
- **Course Management**: Admins can add, update, and delete courses.
- **Student Management**: Admins can view and manage student information.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **Python**: The programming language used to build the application.
- **SQLite**: The default database engine used by Django for development.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/pujitha2712/student-course-registration.git

2. **Navigate to the Project Directory**
   ```bash
   cd student-course-registration
3. **Create a Virtual Environment**
   ```bash
   python -m venv venv

4. **Install the required packagest**
    ```bash
   pip install -r requirements.txt

    
5. Open weather_project/settings.py and add your API key and other configuration settings as needed.
   
6. **Run database migrations**
    ```bash
   python manage.py migrate
7. **Start the development server**
    ```bash
    python manage.py runserver

8.Visit the application
Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.
Usage
Student Registration: Navigate to the registration page to create a new student profile.
Course Registration: Once logged in, go to the course registration page to enroll in courses.
Admin Panel: Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage students and courses. Default admin credentials can be created by running python manage.py createsuperuser and following the prompts.
Contributing
If you want to contribute to this project, please fork the repository and create a pull request with your changes. Make sure to follow the code style and conventions used in the project.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, please contact me at pujithadr@outlook.com.

You can customize this README based on the specific features and setup of your project. Make sure to replace placeholder texts with your actual project details and instructions.



