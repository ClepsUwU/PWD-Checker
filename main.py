
def check_password(pwd):
    min_len = 8
    as_upper = False
    as_lower = False
    as_digit = False
    as_special_character = False
# Vérifie si l'input de l'utilisateur contient une majuscule, minuscule, un chiffre et un caractère special
    if len(pwd) >= min_len:
        for caractere in pwd:
            if caractere.isupper():
                as_upper = True     
            elif caractere.islower():
                as_lower = True
            elif caractere.isdigit():
                as_digit = True
            elif caractere in "!@#$%^&*()-_+=<>?/":
                as_special_character = True
# Si l'input de l'utilisateur contient tout les attributs nécessaire pour trigger True, alors le mot de passe est assez fort, si il manque un attribut
# Alors le mot de passe est pas assez fort
        if all([as_upper, as_lower, as_digit, as_special_character]):
            return True
        else:
            return False
    else:
        return False

# Visu de l'utilisateur

mot_de_passe = input("Entrez un mot de passe pour vérifier sa force: ")
if check_password(mot_de_passe):
    print("Le mot de passe est assez fort.")
else:
    print("Le mot de passe n'est pas assez fort.")