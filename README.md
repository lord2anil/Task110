# Django Project

This is a Django project that includes an API for fetching Bitcoin prices and interacting with a LLaMA model.

## Project Structure


## Setup

1. **Clone the repository:**
   

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

### Chat Endpoint

- **URL:** `/api/chat/`
- **Method:** `POST`
- **Description:** Interacts with the LLaMA model and fetches Bitcoin prices based on user messages.

#### Example Request
```json
{
    "message": "What is the current Bitcoin price?"
}

{
    "response": "The current price of Bitcoin is $50000"
}

Rate Limiting
The API has a rate limit of 3 requests per minute per IP address. If the limit is exceeded, the following response is returned:

{
    "error": "Rate limit exceeded. Try again later."
}