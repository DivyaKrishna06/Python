def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True   #out of loop if true/yes

        if ok in ('n', 'no', 'nop', 'nope'):
            return False 
        retries = retries - 1

        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)   # keep repeating until yes

resp=input('Do you really want to quit: ')
ask_ok(resp)