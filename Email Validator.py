import re
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None
email_input = input("Enter an email address to validate:")
if is_valid_email(email_input):
    print("Valid email address!")
else:
    print("Invalid email address")
