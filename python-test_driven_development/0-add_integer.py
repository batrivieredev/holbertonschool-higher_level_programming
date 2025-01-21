#!/usr/bin/python3
"""
Ce module fournit une fonction `add_integer` qui additionne deux entiers ou
flottants, en les convertissant en entiers si nécessaire.
"""


def add_integer(a, b=98):
    """Additionne deux entiers ou flottants,
      en les convertissant en entiers si nécessaire.

    Args:
        a (int ou float) : Le premier nombre.
        b (int ou float, optionnel) : Le deuxième nombre.
        Par défaut, il est égal à 98.

    Raises:
        TypeError : Si `a` ou `b` n'est ni un entier ni un flottant.

    Returns:
        int : La somme de `a` et `b` sous forme d'entier.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a doit être un entier")
    if not isinstance(b, (int, float)):
        raise TypeError("b doit être un entier")

    # Vérification des valeurs NaN
    if isinstance(a, float) and a != a:  # Vérification NaN
        raise ValueError("a ne peut pas être NaN")
    if isinstance(b, float) and b != b:  # Vérification NaN
        raise ValueError("b ne peut pas être NaN")

    # Vérification du dépassement de capacité pour les flottants (infini)
    if isinstance(a, float) and (a == float('inf') or a == -float('inf')):
        raise OverflowError("a est trop grand pour être converti en entier")
    if isinstance(b, float) and (b == float('inf') or b == -float('inf')):
        raise OverflowError("b est trop grand pour être converti en entier")

    # Conversion en int après validation
    return int(a) + int(b)
