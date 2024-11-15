# Django Project

This is a Django project that includes an API for fetching Bitcoin prices and interacting with a LLaMA model.


## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/lord2anil/Task110.git

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## API Endpoints
### Please Include the Your api key in [utils.py](api/utils.py)

### Chat Endpoint

- **URL:** `/api/chat/`
- **Method:** `POST`
- **Description:** Interacts with the LLaMA model and fetches Bitcoin prices based on user messages.

#### Example Request

```
{
    "message": "fetch the current prize of bitcoin"
}


{
    "response": "The current price of Bitcoin is $50000"
}
```

#### Note-:   For getting the crypto price, the promt should be "fetch the current prize of {crypto Currency Name}"  (case insensitive)   and  other are normal conversation with agent

#### Rate Limiting
The API has a rate limit of 3 requests per minute per IP address. If the limit is exceeded, the following response is returned:

```
{
    "error": "Rate limit exceeded. Try again later."
}
```
#### cache_timeout = 10s   for storing the response for 10 seconds in cache 


### Testing video 

[Demo Video](https://drive.google.com/file/d/1Yb104OSCp671tJ_8ObS28e0l-Hh0qNZY/view?usp=sharing)

