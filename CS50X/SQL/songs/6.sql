SELECT songs.name
FROM songs JOIN artists ON songs.artist_id = artists.id
Where artists.name = "Post Malone";

