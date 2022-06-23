
def emailprocess(email):
    email_username = email[0:email.index("@")]
    #print(f'username is {email_username}')

    email_domain = email[email.index('@') + 1:]
   # #print(f'domain is {email_domain}')
    return [email_username,email_domain]

def print_message(email_username,email_domain):
    print (f'username is :{email_username} ; Mail domain is :{email_domain}')

def main():
    email = input('Please enter your email address :').strip()
    email_domain , email_username = emailprocess(email)
    print_message(email_username,email_domain)

if __name__ == "__main__":
    main()