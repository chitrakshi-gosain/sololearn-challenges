import re

password = input()

if len(password) > 6:
    if re.search(r'.*[0-9]+.*[0-9]+.*',password) and \
        re.search(r'.*[!@#$%&*]{1}.*[!@#$%&*]{1}.*',password):
        print ("Strong")
    else:
        print ("Weak")
else:
    print ("Weak")
