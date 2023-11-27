# Educational ERP System with Online Lecture Creation and Attendance Management

## Project Overview

This comprehensive ERP system is designed to enhance the educational experience by providing a platform for teachers to create and conduct online lectures. The system leverages Django for its robust framework and incorporates Google Authentication for secure access.

### Features

1. **Online Lecture Creation:**
   - Teachers can create and schedule online lectures, specifying date, time, and topic.
   - Upload and share lecture materials, including presentations, documents, and multimedia content.

2. **Student Participation:**
   - Students can join scheduled lectures through the platform.
   - Real-time communication features such as chat or Q&A for student-teacher interaction.

3. **Attendance Tracking:**
   - Automated attendance tracking during online lectures.
   - Ability for teachers to manually mark attendance and make adjustments as needed.

4. **Google Authentication:**
   - Secure user authentication using Google accounts for both teachers and students.
   - Simplifies the registration and login process, ensuring the privacy and security of user data.

5. **User Profiles:**
   - Personalized profiles for teachers and students with essential information.
   - Display of lecture history, attendance records, and other relevant details.

6. **Dashboard and Analytics:**
   - Comprehensive dashboards for teachers to view attendance trends, lecture analytics, and student engagement metrics.

7. **Responsive Design:**
   - Mobile-friendly interface for access on various devices, providing flexibility for both teachers and students.

## Installation and Setup

### Prerequisites

- Python 3.x installed
- Django framework installed (`pip install Django`)
- Google API credentials for authentication

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/educational-erp.git
   cd ncer.herokuapp.com-master
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Google Authentication:**
   - Obtain Google API credentials and configure them in the settings.
   - Update `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in the settings.

4. **Database Setup:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open a web browser and go to `http://127.0.0.1:8000/` to access the application.
   

## Acknowledgments

- Special thanks to the Django and Google API communities for their valuable contributions and support.

## Images

<img width="1467" alt="Screenshot 2023-11-27 at 11 03 34 AM" src="https://github.com/ketanmore2002/ncer.herokuapp.com/assets/88627103/22444499-d796-447a-aa77-6d42380f8b4f">

<img width="1467" alt="Screenshot 2023-11-27 at 11 04 02 AM" src="https://github.com/ketanmore2002/ncer.herokuapp.com/assets/88627103/d2f46d24-1cdf-49fe-86d2-fa6682b8863f">

<img width="1467" alt="Screenshot 2023-11-27 at 11 04 25 AM" src="https://github.com/ketanmore2002/ncer.herokuapp.com/assets/88627103/08e70d85-cf0a-4d74-87e3-cd3b44350b31">

<img width="1467" alt="Screenshot 2023-11-27 at 11 04 50 AM" src="https://github.com/ketanmore2002/ncer.herokuapp.com/assets/88627103/e513fd3f-27d0-4d3c-b526-ccd1d4f3a5b8">

<img width="1467" alt="Screenshot 2023-11-27 at 11 05 24 AM" src="https://github.com/ketanmore2002/ncer.herokuapp.com/assets/88627103/cc3ca86d-0cf9-4b21-b87c-1138e47519fa">

<img width="1467" alt="Screenshot 2023-11-27 at 11 06 51 AM" src="https://github.com/ketanmore2002/ncer.herokuapp.com/assets/88627103/85ffb509-3649-47f9-9a52-9024eb09b7a1">


