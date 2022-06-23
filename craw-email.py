from cutemail import emailprocess,print_message


def main():
    email = ['user.trungio@gmail.com', 'user.lamio@gmail.com','trungopla@outlook.com.vn','trungthitbam@gmail.com']

    for email in email:
        username , user_domain = emailprocess(email)
        print_message(username, user_domain)


if __name__ == "__main__":
    main()