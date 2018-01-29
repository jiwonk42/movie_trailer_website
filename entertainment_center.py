import media
#media: another file that has Movie Class

#media: File Name
#Movie: Class Name 
grinch = media.Movie(
    "How the Grinch Stole Christmas",
    "A grumpy Grinch plots to ruin Christmas for the village of Whoville.",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcT-oosslYzD61pdLgPVmjN53hdzb-bjBeJajr2UILlq7kQNz7jR",
    "https://www.youtube.com/watch?v=myTaigPrbsg")

orphan = media.Movie(
    "Orphan",
    "A husband and wife who recently lost their baby adopt a 9 year-old girl who is not nearly as innocent as she claims to be.",
    "http://www.gstatic.com/tv/thumb/movieposters/193289/p193289_p_v8_aa.jpg",
    "https://www.youtube.com/watch?v=2ywOPNNii9w")

shawshank = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

hannibal = media.Movie(
    "Hannibal",
    " Living in exile, Hannibal Lecter tries to reconnect with now disgraced F.B.I. Agent Clarice Starling, and finds himself a target for revenge from a powerful victim.",
    "http://www.gstatic.com/tv/thumb/movieposters/24118/p24118_p_v8_ad.jpg",
    "https://www.youtube.com/watch?v=Lr3OavheNu0")

cradle = media.Movie(
    "A Hand That Rocks the Cradle",
    "After her humiliated husband kills himself, an embittered pregnant widow loses her child, and embarks on a mission of vengeance against a woman and her family.",
    "http://www.gstatic.com/tv/thumb/movieposters/13677/p13677_p_v8_ae.jpg",
    "https://www.youtube.com/watch?v=0_Lujfdix9A")

#print(orphan.storyline)

grinch.show_trailer()
