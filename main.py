scores = [90,85,100,95,98,96]
total_scores = sum(scores)
amount = len(scores)

print(f'The average quiz score for my chemistry grades are {total_scores / amount}')

# Rapid City = 22.7 miles
# Big Rapids = 88.7 miles
# Detroit = 256 miles
# Gaylord = 60.1 miles
# Lansing = 182
distances = [22.7, 88.7, 256, 60.1,182 ]
min = min(distances)
max = max(distances)
amount_distance = len(distances)
sum_distances = sum(distances)
print(f'The shortest round trip driving distance is between Traverse city and Rapid city with it only being {min} miles')

print(f'The longest round trip driving distance is between Traverse city and Detroit with it being a whopping {max} miles')

print(f'The average drcing distance between all these cities is {sum_distances / amount_distance}')