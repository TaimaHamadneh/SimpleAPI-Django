## First Endpoint:
GET /hello?name={SOME_NAME}

Response should be as application/json like this:
{
  "greeting": "Hello, {SOME_NAME}"
}
If no name is provided, then the response should be:
{ 
   "greeting": "Hello, World!"
}

![image](https://github.com/user-attachments/assets/442be78c-389b-4b87-8db8-8e4914ff257f)
![image](https://github.com/user-attachments/assets/9b602f59-de59-408e-8afa-f45b9e88067e)


## Second Endpoint:
GET /info

Response should as application/json. It should contain the following information:
- Request time formatted in ISO8601
- Client IP Address
- Server/Host name
- Client Request Headers

Example response:
{
  "time": "2024-08-24T14:15:12Z",
  "client_address": "192.168.1.1",
  "host_name": "my-great-server",
  "headers": {
    "Accept": "all",
    "User-Agent": "curl 1/123"
  }
}
![image](https://github.com/user-attachments/assets/cec8e531-bc9a-4e30-8bc2-f4faa6406701)

## Project Setup

### Python Version
- Python 3.12.5

### Django Version
- Django 5.1.1


## Running the App Locally:
To set up the development environment and run the Django app locally, follow these steps:

### 1. Clone the Repository:
```
git clone [https://github.com/your-username/your-repository.git](https://github.com/TaimaHamadneh/SimpleAPI-Django/)
cd SimpleAPI-Django
```
### 2. Create a Virtual Environment:
```
python -m venv venv
```
### 3. Activate the Virtual Environment:
On Windows:
```
venv\Scripts\activate
```
### 4. Install Dependencies:
```
pip install django
```
### 5. Apply Migrations:
```
python manage.py migrate
```
### 6. Run the Development Server:
```
python manage.py runserver
```
The app will be available at http://127.0.0.1:8000/.





