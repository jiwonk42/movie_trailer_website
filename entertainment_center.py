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

#print(orphan.storyline)

grinch.show_trailer()
