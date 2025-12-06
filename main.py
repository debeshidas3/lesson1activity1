import random
import string

def generate_password(length=10):
    uppercase = string.ascii_uppercase      
    lowercase = string.ascii_lowercase     
    digits = string.digits          
    
    all_chars = uppercase + lowercase + digits
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

print(generate_password(26))