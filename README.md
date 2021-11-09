# whelp-task

**[Here](https://user-images.githubusercontent.com/54992849/140647396-150aea1c-eed4-42cf-bda6-c178517423fb.mp4) is the live demonstration of endpoints and celery worker along with RabbitMQ**

Before running the application make sure that you have your API key from ipdata.co website in your .env file which this project uses it under the hood to get the details about specific ip address.
Also before running the test cases, make sure you create a user with following details:

```js
{
    "age": 21,
    "name": "Yalchin",
    "surname": "Mammadli",
    "username": "Yalchin405",
    "email": "yalchinmammadli@yalchin.info",
    "gender": "M",
    "password": "Yalcin-1"
}
```

Docs for all the endpoints are available in the https://localhost:5000/docs (make sure to change port if you run the application on different port) if you run the application locally.

To install all the dependencies execute `pip install -r reqs.txt`

To run the test cases execute `pytest` in the main directory, and make sure application is running.

To run the application execute `docker-compose up -d`
