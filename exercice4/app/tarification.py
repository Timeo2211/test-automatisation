def prix_inscription(nb_cours: int) -> float:
    prix_unitaire = 40
    total = nb_cours * prix_unitaire
    if nb_cours >= 3:
        total = round(total * 0.85, 2)
    return float(total)
