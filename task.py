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
    """
        Calcola il limite di una espressione matematica e gestisce
        il caso in cui il limite non esiste.

        Parametri:
        espressione (str): la funzione, es. "1/x"
        variabile (str): la variabile, es. "x"
        punto (str): il punto, es. "0", "oo", "-oo"

        Ritorna:
        Il valore del limite oppure un messaggio esplicativo
        """

    try:
        # 1. Variabile simbolica
        var = sp.Symbol(variabile)

        # 2. Espressione simbolica
        expr = sp.sympify(espressione)

        # 3. Punto
        if punto == "oo":
            punto_sym = sp.oo
        elif punto == "-oo":
            punto_sym = -sp.oo
        else:
            punto_sym = sp.sympify(punto)

        # 4. Calcolo limiti destro e sinistro (utile per verificare esistenza)
        limite_dx = sp.limit(expr, var, punto_sym, dir='+')
        limite_sx = sp.limit(expr, var, punto_sym, dir='-')

        # 5. Controllo se il limite esiste
        if limite_dx == limite_sx:
            # Caso: limite esistente
            if limite_dx == sp.oo:
                return "Il limite è +infinito"
            elif limite_dx == -sp.oo:
                return "Il limite è -infinito"
            else:
                return limite_dx
        else:
            # Caso: limite NON esiste
            return f"Il limite non esiste (dx={limite_dx}, sx={limite_sx})"

    except Exception as e:
        return f"Errore nel calcolo: {e}"

    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""

    x = sp.Symbol(variabile)
    f = sp.sympify(espressione)

    polinomio = 0

    for n in range(ordine + 1):
        derivata = sp.diff(f, x, n)
        derivata_val = derivata.subs(x, punto)
        termine = (derivata_val / sp.factorial(n)) * (x - punto) ** n
        polinomio += termine

    # Espande completamente il polinomio
    polinomio = sp.expand(polinomio)

    # Riordina i termini dal grado più alto al più basso
    polinomio = sp.Poly(polinomio, x).as_expr()

    return polinomio


    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    # Definizione dei simboli
    x = sp.Symbol(var1)
    y = sp.Symbol(var2)

    # Conversione delle stringhe in espressioni SymPy
    expr1 = sp.sympify(eq1)
    expr2 = sp.sympify(eq2)

    # Risoluzione con linsolve
    sol_set = sp.linsolve([expr1, expr2], (x, y))

    # Analisi del risultato
    if not sol_set:
        return {"errore": "Nessuna soluzione"}

    soluzione = list(sol_set)[0]

    # Controllo infinito soluzioni (parametri liberi)
    if any(s.has(sp.Symbol) for s in soluzione):
        return {"errore": "Infinite soluzioni"}

    # Costruzione dizionario finale
    return {x: soluzione[0], y: soluzione[1]}

    pass

def main():
    print("Sub-task 1:", calcola_derivata("exp(x)", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 1))
    print("Sub-task 3:", calcola_limite("(x**2 - 1)/(x - 1)", "x", "1"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("2*x + y - 5", "x + 3*y - 5", "x", "y"))

if __name__ == "__main__":
    main()


