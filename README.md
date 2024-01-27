# SMART ATTENDANCE SYSTEM

This web application incorporates machine learning, Django, and OpenCV to facilitate a user attendance system with advanced features.

## Features

- **Face Recognition**: Utilizes OpenCV and a KNN classifier for accurate and efficient user identification through facial recognition.
- **Secure User Registration**: Implements a secure user registration process with two-factor email authentication to enhance account security.
- **Robust User Login System**: Utilizes Django's inbuilt authenticator to establish a secure login system, ensuring only authorized access to the application.

## Tech Stack

- Python
- Django
- OpenCV
- SQLite
- HTML
- CSS

  ## Installation

To run the Smart Attendance System locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/priyanshusingh302/Attendance-using-ML.git
```

2. Navigate to the project directory:
```bash
cd Attendance-using-ML
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

