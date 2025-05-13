def calculate_tip(amount, rating):
    """
    Función que calcula cuanta propina se debe dejar

    @param amount:
    @param rating:
    @return:
    """
    rating = rating.lower()

    if rating == "terrible":
        return 0
    elif rating == "poor":
        return round(amount * 0.05)
    elif rating == "good":
        return round(amount * 0.10)
    elif rating == "great":
        return round(amount * 0.16)
    elif rating == "excellent":
        return round(amount * 0.20)
    else:
        return "Rating not recognised"