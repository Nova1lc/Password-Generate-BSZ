import random
import string

banner = '''
+++++++++++++++++++++++++++++
+                              +
+   Password Generator BSZ!   +
+                              +
+++++++++++++++++++++++++++++
'''
print(banner)

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

length = 12
print(generate_password(length))