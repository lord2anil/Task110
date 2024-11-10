from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.
from api.utils import fetch_bitcoin_price,llama_request,rate_limit

from rest_framework.views import APIView

from rest_framework.response import Response


class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get("message").lower()
        
        # Storing the conversation history in session for the 
        
         
        conversation_history = request.session.get("conversation_history")
        if conversation_history is None:
            conversation_history = []
        conversation_history.append({"role": "user", "content": user_message})
        
        # Determine response based on keywords
        
        if "bitcoin price" in user_message :
            # Fetch Bitcoin price and return
            #checking the rate limit
            is_allowed, rate_limit_response = rate_limit(request)
            if not is_allowed:
                return Response({"error":rate_limit_response})
            price = fetch_bitcoin_price()
            if "Error" in price:
                response = "Error fetching Bitcoin price"
            else:
                response = f"The current price of Bitcoin is ${price}"
                conversation_history.append({"role": "user", "content": response})
                
                
        
        else:
            response=llama_request(conversation_history)
            
        conversation_history.append({"role": "assistant", "content": response})
        request.session["conversation_history"] = conversation_history
        return Response({"response": response})

    
