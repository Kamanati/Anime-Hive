import os,sys,pyfiglet

import os.path
import re
import email.utils

def is_valid_email(email_address):
    # Use regular expression to validate the syntax of the email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email_address):
        return False

    # Use email.utils to parse the email address
    parsed_email = email.utils.parseaddr(email_address)
    if parsed_email[1] == '':
        return False

    return True

# Check if the email file already exists
if os.path.exists("email.txt"):
    with open("email.txt", "r") as f:
        email_address = f.read().strip()
else:
    # Display a note to the user
    print("NOTE:\n By entering your email address, you can access to all details and deep details with no restrictions We Recamond to use Gmail Address.\n")

    # Ask the user for an email address
    email_address = input("Please enter your Gmail address : ")

    # Validate the email address
    if is_valid_email(email_address):
        # Save the email address to a file
        with open("email.txt", "w") as f:
            f.write(email_address)
        print(f"\nYour valid email address: {email_address}")
    else:
        print("\nThe email address you entered is invalid.")
        sys.exit(0)

while(1): 
   logo_text = "Anime-Hive" 
   logo_ascii = pyfiglet.figlet_format(logo_text) 
   print(logo_ascii) 
   print("simple tool to get anime detials") 
   print("") 
   print("""
Select The Option :

1. Search
2. Filter
3. genres Filter
4. Advance Filter
5. download
6. about
7. exit
""")
   suo=input("Select The Options : ")
   if suo == '1':
      os.system('python some.py')
   elif suo == '2':
      os.system('python filter1.py')
   elif suo == '3':
      os.system('python filter2.py')
   elif suo == '4':
      os.system('python ulfil.py')
   elif suo == '5':
      print("")
      print("Iam working hard on this It will ready soon....!")
      print("")
      print("Any query mail me at hasanfq818@gmail.com")
      print("")
      sksj = input("press any key to continue.......")
   elif suo == '6':
      os.system('python about.py')
   elif suo == '7':
      sys.exit(0)
   else:
      print("")
      print("invalid option...")

