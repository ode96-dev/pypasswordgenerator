import string
import secrets

def contains_upper(password:str)->bool:
    for char in password:
        if char.isupper():
            return True
        
        return False
    
def contains_symbols(password:str)->bool:
    for char in password:
        if char in string.punctuation:
            return True
        
        return False
    
def generate_password(length:int, symbols:bool, uppercase:bool )->str:
    combination:str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    gen_password:str = ''

    for _ in range(length):
        gen_password += combination[secrets.randbelow(combination_length)]

    return gen_password


if __name__ == '__main__':
    for i in range(1,6):
        gen_password: str = generate_password(length=10, symbols=True, uppercase=True)
        specs:str = f'Uppercase: {contains_upper(gen_password)}, Symbols:{contains_symbols(gen_password)}'
        print(f"{i}->{gen_password} ({specs})")
        print(gen_password)
