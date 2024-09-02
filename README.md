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
![image](https://github.com/user-attachments/assets/9e6cca62-df56-44ba-875a-a8b259992c9d)
