prefectures = ['Hokkaido', 'Hokkaido', 'Tokyo', 'Kanagawa']
cities = ['Spporo', 'Hakdate', 'Minato', 'Yokohama']
populations = [100, 200, 300, 400]
population_dict = {(state, city): population for state, city, population in zip (prefectures, cities, populations)}
print(population_dict)

I = 3
J = 3
multiplicated_xy_dict = {i:{j:(i*j) for j in range(J)} for i in range(I)}
print(multiplicated_xy_dict)
