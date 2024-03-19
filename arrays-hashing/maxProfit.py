def maxProfit(prices):
    sorted_prices = sorted(prices)
    print(sorted_prices)
    sorted_prices.pop()
    print(sorted_prices)

    lowest_price_index = None

    highest_price = sorted_prices[0]
    highest_price_index = None

    for i in range(len(prices)):
        if lowest_price_index == None and prices[i] == sorted_prices[0]:
            lowest_price_index = i
            continue

        if prices[i] > highest_price and lowest_price_index != None:
            highest_price = prices[i]
            highest_price_index = i

    
        # else:
        #     if prices[i] > highest_price:
        #         highest_price = prices[i]
        #         highest_price_index = i
        #     continue


    return highest_price_index



# prices = [7,1,5,3,6,4]
# sorted_prices = [1, 3, 4, 5, 6, 7]

prices = [7,1,5,3,6,4]

print(maxProfit(prices))