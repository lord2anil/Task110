
import requests
from django.core.cache import cache
from together import Together
from django.core.cache import cache
from django.http import JsonResponse
from datetime import timedelta

TOGETHER_AI_API_URL = "https://api.together.xyz/llama"  
CRYPTO_API_URL = "https://api.coincap.io/v2/assets/bitcoin"     

client = Together(api_key="your_api_key")


def fetch_bitcoin_price():
    
    # Storing the bitcoin_price in  Cache
    cache_key = "bitcoin_price"
    
    
    cache_timeout = 10  
    
    if cache.get(cache_key):
        return cache.get(cache_key)
    
    try:
        response = requests.get(f"{CRYPTO_API_URL}")
        response.raise_for_status()
        price = response.json().get("data", {}).get("priceUsd")
        
        # Storing the bitcoin_price in cache
        
        cache.set(cache_key, price, timeout=cache_timeout)
        return response.json().get("data", {}).get("priceUsd")
    except requests.RequestException as e:
        return f"Error fetching Bitcoin price: {str(e)}"


def llama_request(conversation_history):
    try:
        # Send the conversation history to the LLaMA model
        print(conversation_history)
        response = client.chat.completions.create(
            model="meta-llama/Llama-Vision-Free",
            messages=conversation_history,
            max_tokens=None,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>", "<|eom_id|>"],
            stream=True
        )
        result = ""
        for chunk in response:
            if hasattr(chunk, 'choices') and chunk.choices:
                result += chunk.choices[0].delta.content  # Append the content of each chunk to result

    
        return result

    except Exception as e:
        return f"Error with LLaMA request: {str(e)}"




# Only 3 request  per min
def rate_limit(request, limit=3, period=60):
    """
    Limits the number of requests a user can make within a specified time window.

    :param request: Django request object
    :param limit: Number of allowed requests within the period
    :param period: Time window in seconds
    :return: (bool, JsonResponse or None) - (is_allowed, response if limited)
    """
    user_ip = request.META.get("REMOTE_ADDR")  

    # Construct cache key for tracking requests by IP
    cache_key = f"rate_limit:{user_ip}"
    
    # Check current request count and update cache
    requests_made = cache.get(cache_key, 0)

    if requests_made >= limit:
        return False,"Rate limit exceeded. Try again later."
    
    # Increment request count and set expiration if it's the first request
    cache.set(cache_key, requests_made + 1, timeout=period)

    return True, ""


