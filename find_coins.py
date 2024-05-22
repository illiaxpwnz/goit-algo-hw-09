def find_coins(amount, coins=[50, 25, 10, 5, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result
