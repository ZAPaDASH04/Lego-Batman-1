from BaseClasses import Location

class LB1Location(Location):
    game: str = "Lego Batman: The Videogame"


base_location_id: int = 400000

minikit_location_table: dict[str, int] = {
    "You can Bank on Batman: Minikit 1 - Inside Garage": base_location_id + 100,
    "You can Bank on Batman: Minikit 2 - Above Garage": base_location_id + 101,
    "You can Bank on Batman: Minikit 3 - Behind Glass Window near Spawn": base_location_id + 102,
    "You can Bank on Batman: Minikit 4 - Mind Control Behind Van in Toxic Waste": base_location_id + 103,
    "You can Bank on Batman: Minikit 5 - In Sewer Grate": base_location_id + 104,
    "You can Bank on Batman: Minikit 6 - In High Window by Cement Mixer": base_location_id + 105,
    "You can Bank on Batman: Minikit 7 - On Balcony Behind Heavy Item near Downward Slope": base_location_id + 106,
    "You can Bank on Batman: Minikit 8 - From Hazard Recycler": base_location_id + 107,
    "You can Bank on Batman: Minikit 9 - Park Two Cars": base_location_id + 108,
    "You can Bank on Batman: Minikit 10 - from Destroying Five Phone Booths": base_location_id + 109,

    # "An Icy Reception: Minikit 1 - On Ledge near Spawn": base_location_id + 110,
    # "An Icy Reception: Minikit 2 - Behind Boarded Window on Ledge near Spawn": base_location_id + 111,
    # "An Icy Reception: Minikit 3 - In Silver Icecream Stand": base_location_id + 112,
    # "An Icy Reception: Minikit 4 - Behind Icecream Truck": base_location_id + 113,
    # "An Icy Reception: Minikit 5 - In Alley with Hostage": base_location_id + 114,
    # "An Icy Reception: Minikit 6 - In Silver Canisters Above Icecream Cones": base_location_id + 115,
    # "An Icy Reception: Minikit 7 - In Female Locked Room": base_location_id + 116,
    # "An Icy Reception: Minikit 8 - In Silver Object Behind Toxic Gas": base_location_id + 117,
    # "An Icy Reception: Minikit 9 - In Vent with Fan": base_location_id + 118,
    # "An Icy Reception: Minikit 10 - In Hypnosis Room": base_location_id + 119,
    #
    # "Two-Face Chase: Minikit 1 - Destroy Three Dumpsters": base_location_id + 120,
    # "Two-Face Chase: Minikit 2 - In Manhole Cover": base_location_id + 121,
    # "Two-Face Chase: Minikit 3 - Destroy Southwest Trash Dumpster": base_location_id + 122,
    # "Two-Face Chase: Minikit 4 - Destroy Three Cars": base_location_id + 123,
    # "Two-Face Chase: Minikit 5 - Destroy North Supports": base_location_id + 124,
    # "Two-Face Chase: Minikit 6 - Destroy South Supports": base_location_id + 125,
    # "Two-Face Chase: Minikit 7 - Use Joker's Van Panel": base_location_id + 126,
    # "Two-Face Chase: Minikit 8 - Use Harley's Truck Panel": base_location_id + 127,
    # "Two-Face Chase: Minikit 9 - In Telephone Booth": base_location_id + 128,
    # "Two-Face Chase: Minikit 10 - Destroy Three Food Carts": base_location_id + 129,
    #
    # "A Poisonous Appointment: Minikit 1 - Destroy All Carrots": base_location_id + 130,
    # "A Poisonous Appointment: Minikit 2 - On Top of Trees": base_location_id + 131,
    # "A Poisonous Appointment: Minikit 3 - In Heated Greenhouse": base_location_id + 132,
    # "A Poisonous Appointment: Minikit 4 - Above Orange Flowers": base_location_id + 133,
    # "A Poisonous Appointment: Minikit 5 - By Rail above Potted Plant": base_location_id + 134,
    # "A Poisonous Appointment: Minikit 6 - In Underwater Pipe": base_location_id + 135,
    # "A Poisonous Appointment: Minikit 7 - In Vat near Second Pitcher Plant": base_location_id + 136,
    # "A Poisonous Appointment: Minikit 8 - Destroy 3 Carrots": base_location_id + 137,
    # "A Poisonous Appointment: Minikit 9 - Above Heated Pipes": base_location_id + 138,
    # "A Poisonous Appointment: Minikit 10 - In Toxic Waste Room Above Ledge": base_location_id + 139,
    #
    # "The Face-Off: Minikit 1 - Jump on 5 Poles": base_location_id + 140,
    # "The Face-Off: Minikit 2 - In Grapple Point to Right of Spawn": base_location_id + 141,
    # "The Face-Off: Minikit 3 - Build Dollar Sign": base_location_id + 142,
    # "The Face-Off: Minikit 4 - In Revolving Door": base_location_id + 143,
    # "The Face-Off: Minikit 5 - On Roof Above Recycler": base_location_id + 144,
    # "The Face-Off: Minikit 6 - In the Toxic Waste Room Pipe": base_location_id + 145,
    # "The Face-Off: Minikit 7 - Underneath the Toxic Waste near the Three Platform Bridge": base_location_id + 146,
    # "The Face-Off: Minikit 8 - On Right Side of Toxic Waste Room": base_location_id + 147,
    # "The Face-Off: Minikit 9 - On Right Side of Vault Room": base_location_id + 148,
    # "The Face-Off: Minikit 10 - Destroy Five Chests": base_location_id + 149,
    #
    # "There She Goes Again: Minikit 1 - In Female Locked Room": base_location_id + 150,
    # "There She Goes Again: Minikit 2 - Drive Car Into Garage": base_location_id + 151,
    # "There She Goes Again: Minikit 3 - Locked Underwater Behind Fence": base_location_id + 152,
    # "There She Goes Again: Minikit 4 - Destroy Three Carrots": base_location_id + 153,
    # "There She Goes Again: Minikit 5 - Locked Underwater by Blue Pump": base_location_id + 154,
    # "There She Goes Again: Minikit 6 - Lawnmowing Flowers": base_location_id + 155,
    # "There She Goes Again: Minikit 7 - Behind Window Above Dumpster": base_location_id + 156,
    # "There She Goes Again: Minikit 8 - Behind Second Dumpster Under Water Tower": base_location_id + 157,
    # "There She Goes Again: Minikit 9 - In Glass Roof": base_location_id + 158,
    # "There She Goes Again: Minikit 10 - In Pipe After Breaking Glass": base_location_id + 159,
    #
    # "Batboat Battle: Minikit 1 - Turn on Lighthouse": base_location_id + 160,
    # "Batboat Battle: Minikit 2 - Blow Up Silver Box": base_location_id + 161,
    # "Batboat Battle: Minikit 3 - Sink the Ship": base_location_id + 162,
    # "Batboat Battle: Minikit 4 - Pull the Pipe": base_location_id + 163,
    # "Batboat Battle: Minikit 5 - In Alcove Surrounded by Ice": base_location_id + 164,
    # "Batboat Battle: Minikit 6 - In Silver Crate Surrounded by Toxic Water": base_location_id + 165,
    # "Batboat Battle: Minikit 7 - Destroy Silver Around Pipe": base_location_id + 166,
    # "Batboat Battle: Minikit 8 - Destroy Three Buoys": base_location_id + 167,
    # "Batboat Battle: Minikit 9 - In Corner Surrounded by Ice": base_location_id + 168,
    # "Batboat Battle: Minikit 10 - Destroy Three Silver Boxes in Toxic Water": base_location_id + 169
}

hostage_location_table: dict[str, int] = {
    "You Can Bank On Batman: Hostage": base_location_id + 400,
    # "An Icy Reception: Hostage" base_location_id + 401,
    # "A Poisonous Appointment: Hostage", base_location_id + 402,
    # "The Face-Off: Hostage", base_location_id + 403,
    # "There She Goes Again: Hostage", base_location_id + 404,
    # "Under The City: Hostage", base_location_id + 405,
    # "Zoo's Company: Hostage", base_location_id + 406,
    # "Penguin's Lair: Hostage", base_location_id + 407,
    # "Joker's Home Turf: Hostage", base_location_id + 408,
    # "Little Fun at the Big Top: Hostage", base_location_id + 409,
    # "In the Dark Night: Hostage", base_location_id + 410,
    # "To the Top of the Tower: Hostage", base_location_id + 411,
    # "The Riddler Makes a Withdrawal: Hostage", base_location_id + 412,
    # "On the Rocks: Hostage", base_location_id + 413,
    # "Green Fingers: Hostage", base_location_id + 414,
    # "An Enterprising Theft: Hostage", base_location_id + 415,
    # "Breaking Blocks: Hostage", base_location_id + 416,
    # "Rockin' the Docks: Hostage", base_location_id + 417,
    # "Stealing the Show: Hostage", base_location_id + 418,
    # "A Daring Rescue: Hostage", base_location_id + 419,
    # "Arctic World: Hostage", base_location_id + 420,
    # "A Surprise for the Commissioner: Hostage", base_location_id + 421,
    # "The Joker's Masterpiece: Hostage", base_location_id + 422,
    # "The Lure of the Night: Hostage", base_location_id + 423,
    # "Dying of Laughter: Hostage", base_location_id + 424,
}

location_table = {
    **minikit_location_table,
    **hostage_location_table
}
