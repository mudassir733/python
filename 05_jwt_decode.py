import jwt
import base64
import os
from dotenv import load_dotenv


load_dotenv()

def decode_jwt(token):
    print("Token to decode:", token)  
    parts = token.split('.')
    if len(parts) != 3:
        raise ValueError("Invalid JWT token format. Expected 3 parts separated by dots.")
    
    header, payload, signature = parts
    
   
    header_decoded = base64.urlsafe_b64decode(header + '==').decode('utf-8')
    payload_decoded = base64.urlsafe_b64decode(payload + '==').decode('utf-8')
    
    return {
        'header': header_decoded,
        'payload': payload_decoded,
        'signature': signature
    }

if __name__ == '__main__':
    token = os.getenv("JWT_TOKEN")
    
    try:
        decoded_jwt = decode_jwt(token)
        print("Decoded Header:", decoded_jwt['header'])
        print("Decoded Payload:", decoded_jwt['payload'])
    except ValueError as e:
        print("Error decoding JWT:", e)
