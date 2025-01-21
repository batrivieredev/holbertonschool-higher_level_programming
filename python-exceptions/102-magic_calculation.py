#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):  # La boucle itère de 1 à 2 (inclus)
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception as e:
            print(f"Exception caught: {e}")
            result = 0  # Réinitialiser result si une exception est levée
            break  # Sortir de la boucle si une exception est levée
    if result == 0:  # Si la boucle a été interrompue par une exception
        result = b + a
    return result
