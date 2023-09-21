user_name= input('Enter your name: ')
user_pwd= input('Enter your password:')
pwd_len= int(len(user_pwd))
pwd_hidden= '*' * pwd_len
print (f'{user_name}, your password {pwd_hidden} lenght is {pwd_len}')