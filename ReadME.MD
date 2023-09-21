### Flow of Application

## Run application Using Docker

**Basic Requirements**
 - Docker version 20.10.21, build 20.10.21-0ubuntu1~20.04.2
 - Docker Compose version v2.20.2

**Application Run via Docker Commands**
  - NOTE: Make sure you are is same as docker-compose.yml file path.
  
  - Command: **docker-compose up --build**



## Run Application's Frontend and Backend manually
**NOTE:**
- If in your system's **pip** version is 3 or 3+ so you have to use **pip3** instend of **pip** in all the commands and **python** version is 3 or 3+ you have to use **python3** instend of **python** in all the commands.

- Make sure frontend run on **5000** port and Backend run on **8000** port.


**Application run manually**
- Backend run commands
    - **pip install -r requirements.txt**
    - **python manage.py makemigrations app**
    - **python manage.py migrate**
    - **python manage.py runserver**

      Backend start successfully.

      Backend Swagger API Documentation URL: http://127.0.0.1:8000/swagger/

- Frontend run commands
    - **python -m http.server 5000**

      Frontend start successfully.

      Frontend Main page URL: http://127.0.0.1:5000/frontend/index.html


- Landing Page: http://127.0.0.1:5000/frontend/index.html
- Login Page: http://127.0.0.1:5000/frontend/login.html
- Register Page: http://127.0.0.1:5000/frontend/register.html
- Dashboard Page: http://127.0.0.1:5000/frontend/dashboard.html
