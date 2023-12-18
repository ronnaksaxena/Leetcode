class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating = {}
        self.highestRating = collections.defaultdict(list) # {cuisine: [(-rating, name)]}
        self.foodToCuisine = {}
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.rating[f] = r
            heapq.heappush(self.highestRating[c], (-r, f))
            self.foodToCuisine[f] = c
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = newRating
        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.highestRating[cuisine], (-newRating, food))
        return
        

    def highestRated(self, cuisine: str) -> str:
        rate, name = self.highestRating[cuisine][0]
        while -rate != self.rating[name]:
            heapq.heappop(self.highestRating[cuisine])
            rate, name = self.highestRating[cuisine][0]
        return name
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)