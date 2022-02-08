FILE_NAME = "10-million-password-list-top-1000000.txt"
NORMAL_LENGHT = 8

special_chars = [
    '+','-','/','\\',
    '*','.',',',';',
    '<','>','_','@',
    '#','$','%','&',
    '{','}','`','~',
    '˛','(',')','ß',
    '[',']','!','?',
    '§','˘','°','=',
    'ł','Ł','|','€',
    '÷','¨','^'
]

result = {
    "is_on_password_list": False,
    "is_lenght_normal": False,
    "length": 0,
    "special_charachters": 0,
    "numbers_in_pwd": 0,
    "lowercase": 0,
    "uppercase": 0,
    "description": ""
}

def load_password_list():
    passwords = []
    with open(FILE_NAME,'r') as password_file:
        for password in password_file:
            passwords.append(password.strip('\n'))

    print("most common password list size is {}".format(len(passwords)))
    return passwords

def check_existance_in_list(password, most_common_passwords):
    if password in most_common_passwords:
        result["is_on_password_list"] = True

def check_lenght(password):
    if len(password) < NORMAL_LENGHT:
        result["is_lenght_normal"] = False
    else:
        result["is_lenght_normal"] = True
    result['length'] = len(password)

def check_special_charachters(password, special_characters):
    counter = 0
    for charachter in password:
        if charachter in special_characters:
            counter += 1
    result['special_charachters'] = counter

def handle_lowercase_uppercase(password):
    lowercase_counter = 0
    uppercase_counter = 0
    for character in password:
        if character.islower():
            lowercase_counter += 1
        if character.isupper():
            uppercase_counter += 1
    result['lowercase'] = lowercase_counter
    result['uppercase'] = uppercase_counter

def count_numbers(password):
    counter = 0
    for character in password:
        if character.isnumeric():
            counter += 1
    result['numbers_in_pwd'] = counter

def generate_description():
    description = ""
    if result['is_on_password_list']:
        description += "Your password is in the list of most common passwords\n"
    if result['length'] < NORMAL_LENGHT:
        description += "Normal lengh should be 8 charaters not {0}\n".format(result['length'])
    if result['special_charachters'] == 0:
        description += "You should use special characters in your password\n"
    if result['uppercase'] ==  0:
        description += "Use at least one uppercase letter\n"
    if  result['lowercase'] == 0:
        description += "Use at least one lowercase letter\n"
    if result['numbers_in_pwd'] == 0:
        description += "Use numbers in your password\n"
    result['description'] = description

def print_output():
    output = "Result\n"
    output += "Exists in common password list {0}\n".format(result['is_on_password_list'])
    output += "Normal password lenght {0}\n".format(result['is_lenght_normal'])
    output += "Length {0}\n".format(result['length'])
    output += "Lowercase number {0}\n".format(result['lowercase'])
    output += "Uppercase number {0}\n".format(result['uppercase'])
    output += "Special character number {0}\n".format(result['special_charachters'])
    output += "Numbers in password {0}\n".format(result['numbers_in_pwd'])
    output += result['description']
    print(output)


most_common_passwords = load_password_list()
exitMode = False

while not exitMode:
    print("1.Password scanning\n2.Exit")
    choice = input("Enter your choice (1 or 2):")
    if (int(choice) == 1):
        print("Scanning started...")
        password = input("Enter your password for the scanning:")
        check_existance_in_list(password, most_common_passwords)
        check_lenght(password)
        check_special_charachters(password, special_chars)
        count_numbers(password)
        handle_lowercase_uppercase(password) 
        generate_description()
        print_output()
    else :
        exitMode = True
