prices = [int(i) for i in input().rstrip().split(' ')]
n = len(prices)

template = {
    "buy": None,
    "sell": None
}
transaction =list()

def buy_sell(prices, n):
    if n <= 1:
        return 'Invalid'
    for i in range(n):
        while i < n-1 and prices[i] >= prices[i+1]:
            i+=1

        template['buy'] = i
        i+=1

        if i==n-1:
            break

        while i<n and prices[i]>prices[i-1]:
            i += 1

        template['sold'] = i
        i+=1

    transaction.append(template)

buy_sell(prices, n)

print(transaction)

