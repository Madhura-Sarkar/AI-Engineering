fav_movies = ["The Avengers", "Parasite", "3 Idiots", "The Avengers: Age of Ultron", "The Avengers: Endgame"]
print(fav_movies[3])

marks = [80, 75, 90]
marks.append(95)
print(marks)

cities = ["Kolkata", "Delhi", "Mumbai"]
for city in cities:
    print(city)

    numbers = [100, 200, 300, 400, 500]

print(numbers[0:5])
print(numbers[-2])
print(numbers[-4])
print(numbers[1:-1]) 
#it will print the elements from index 1 to index 3 (excluding index 4) 
# even though -1 is the last index of the list. 
# It will not include the last index in the output.