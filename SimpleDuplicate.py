import os
###########################################
# function to remove duplicate emails
def remove_duplicate():
    # opens emails.txt in r mode as one long string and assigns to var
    emails = open(iii, 'r').read()
    # .split() removes excess whitespaces from str, return str as list
    emails = emails.split()
    # empty list to store non-duplicate e-mails
    clean_list = []
    # for loop to append non-duplicate emails to clean list
    for email in emails:
        if email not in clean_list:
            clean_list.append(email)
    return clean_list
    # close emails.txt file
    emails.close()
# assigns no_duplicate_emails.txt to variable below
os.system('cls' if os.name == 'nt' else 'clear')
iii = input(" || Enter Name Text File : ")
bbb = input(" || Save To : ")
no_duplicate_emails = open(bbb, 'w')

# function to convert clean_list 'list' elements in to strings
for email in remove_duplicate():
    # .strip() method to remove commas
    email = email.strip(',')
    no_duplicate_emails.write(f"{email}\n")
# close no_duplicate_emails.txt file
no_duplicate_emails.close()
print(" || DONE ...!!")
quit()
