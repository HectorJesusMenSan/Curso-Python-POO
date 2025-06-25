def max_profitt(prices):
    """
    Calcula la mayor ganancia posible a partir de una lista de precios,
    comprando primero y vendiendo después.


    Retorna:
    La ganancia máxima que se puede obtener al comprar y luego vender.

    """
    if len(prices) < 2:
        raise ValueError("Se requieren al menos dos precios para realizar una operación de compra/venta.")

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit
