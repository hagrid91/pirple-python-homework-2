
Genre = "Romance"
Singer = "Sid Sriram"
year = 2018

def Genre_song():
    print("Genre of song is {one}".format(one = Genre))

def Singer_song():
    print("Artist of the song:{one}".format(one = Singer))

def year_song():
    print("Year the song was released: {one}".format(one = year))

def check(num):
    return(bool(num%2==0))

Genre_song()
Singer_song()
year_song()

num=9
output = check(num)
print(output)
