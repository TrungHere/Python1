
import string
import random

LETTERS = string.ascii_letters 
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation
def get_password_length ():
    password_length = input('how long do u want your password : ')
    return int(password_length)
    
def password_generator(length=8):
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATIONS}"
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choice(printable, k=length)
    random_password = ''.join(random_password)
    return random_password



def main():
    
    password_length = get_password_length()
    password = password_generator(password_length)
    print(Password)
if __name__ == "__main__":
    main()