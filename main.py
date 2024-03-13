import string
import argparse
from data import result


def has_charactor_in_password(password, char_list):
    for char in password:
        if char in char_list:
            return 1
    return 0


def check_password(password:str) -> str:
    score = 0
    
    # Check password for validation
    if len(password) >= 10:
        score += 1       
    score += has_charactor_in_password(password, string.ascii_uppercase)
    score += has_charactor_in_password(password, string.ascii_lowercase)
    score += has_charactor_in_password(password, string.digits)
    score += has_charactor_in_password(password, string.punctuation)
    
    return result[score]
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                description="This script help you check password is strong or no?"
            )
    
    parser.add_argument("password", type=str, help="Your Password")
    arg = parser.parse_args()
    
    # Output 
    print(check_password(arg.password))
    print("GoodBye!!!")
    print("hello")
    
