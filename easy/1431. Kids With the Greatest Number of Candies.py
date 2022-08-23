def kids_with_candies(candies, extraCandies):

    max_candies = max(candies)

    return [kids_candies + extraCandies >= max_candies for kids_candies in candies]
