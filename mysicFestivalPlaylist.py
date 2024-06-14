#Task 1: Artist Lineup Compilation
#You are provided with a list of artist names scheduled to perform at different stages of the music festival. Using a loop, compile 
# these artist names into a set to create a unique lineup without duplicates.

#Example Code:

#artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
#unique_artists = set()
#Expected Outcome:
#A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True.

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
for artist in artist_names:
    unique_artists.add(artist)
duplicate_found = len(artist_names) != len(unique_artists)
print("Duplicate playlists found:", duplicate_found)
print("Unique Artists Lineup:", unique_artists)
