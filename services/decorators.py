from django.http import JsonResponse
from functools import wraps
import requests
import os
from dotenv import load_dotenv

from services.request_processor import get_request_data

load_dotenv()
USER_MANAGEMENT_API = os.getenv('USER_MANAGEMENT_API')


def verify_token(inner_function):
    @wraps(inner_function)
    def _wrapped_function(request, *args, **kwargs):
        try:
            data = get_request_data(request)
            token = data.get('token')
            url = f"{USER_MANAGEMENT_API}/validatetoken/"
            response = requests.post(url, json={"token": token})
            if response.status_code == 200:
                json_response = inner_function(request, *args, **kwargs)
                return json_response
            return JsonResponse({"message": "Please login", "code": "480"})
        except:
            return JsonResponse({"message": "Error verifying access token. Please try again", "code": "480"})
    return _wrapped_function

