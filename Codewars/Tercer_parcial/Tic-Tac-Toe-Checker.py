def is_solved(board):
    """
    Evalúa el estado de un tablero de Tic-Tac-Toe 3x3.
    Retorna:
        1 si "X" ganó,
        2 si "O" ganó,
        0 si es empate sin espacios vacíos,
       -1 si aún no termina el juego.
    """

    # Revisa filas y columnas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]  # Ganador en una fila
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]  # Ganador en una columna

    # Revisa diagonales
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # Verifica si hay espacios vacíos
    for row in board:
        if 0 in row:
            return -1  # El juego aún no termina