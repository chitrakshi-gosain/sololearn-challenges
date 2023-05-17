from re import sub

secret_message = input()
secret_message = secret_message[::-1]
print(sub('[^a-zA-Z ]+', '', secret_message))