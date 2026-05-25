import sympy
from typing import Dict
from sympy import symbols, sympify, diff, SympifyError

import sympy as sp

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    """Sub-task 1: Calcolare una Derivata."""

    """
        Calcola la derivata simbolica di un'espressione rispetto a una variabile.

        :param espressione: stringa dell'espressione matematica (es. "x**2 + sin(x)")
        :param variabile: variabile rispetto a cui derivare (es. "x")
        :return: oggetto SymPy rappresentante la derivata
        """
    try:
        # Definizione del simbolo
        var = symbols(variabile)

        # Parsing dell'espressione
        expr = sympify(espressione)

        # Calcolo della derivata
        derivata = diff(expr, var)

        return derivata

    except SympifyError as e:
        raise ValueError(f"Espressione non valida: {espressione}") from e

    except Exception as e:
        raise RuntimeError(f"Errore durante il calcolo della derivata: {e}") from e

    pass

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    """Sub-task 2: Calcolare un Integrale Definito."""

    # Definizione della variabile simbolica
    var = sp.symbols(variabile)

    # Conversione della stringa in espressione simbolica
    expr = sp.sympify(espressione)

    # Calcolo dell'integrale definito
    integrale = sp.integrate(expr, (var, estremo_inf, estremo_sup))

    return integrale

    pass

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("exp(x)", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 1))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
