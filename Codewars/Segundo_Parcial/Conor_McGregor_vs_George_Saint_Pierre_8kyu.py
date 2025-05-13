def quote(fighter: str)->str:
    """
    Función que retorna una frase dependiendo cúal sea el ganador de la pelea.
    @param fighter: Peleador ganador
    @return: Frase
    """
    fighter = fighter.lower()
    if fighter != "conor mcgregor":
        return "I am not impressed by your performance."
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!"