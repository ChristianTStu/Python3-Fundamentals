current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}
print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input('What move would you like a showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Your requested movie isn't currently playing at our theater.")
else:
    print(f'{movie} is playing at {showtime}!')