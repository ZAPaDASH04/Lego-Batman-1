from BaseClasses import Location

class LB1Location(Location):
    game: str = "Lego Batman: The Videogame"


base_location_id = 49000000

minikit_location_table = {
    "You can Bank on Batman: Minikit 1 - Inside Garage", base_location_id + 100,
    "You can Bank on Batman: Minikit 2 - Above Garage", base_location_id + 101,
    "You can Bank on Batman: Minikit 3 - Behind Glass Window near Spawn", base_location_id + 102,
    "You can Bank on Batman: Minikit 4 - Mind Control Behind Van in Toxic Waste", base_location_id + 103,
    "You can Bank on Batman: Minikit 5 - in Sewer Grate", base_location_id + 104,
    "You can Bank on Batman: Minikit 6 - in High Window by Cement Mixer", base_location_id + 105,
    "You can Bank on Batman: Minikit 7 - on Balcony Behind Heavy Item near Downward Slope", base_location_id + 106,
    "You can Bank on Batman: Minikit 8 - from Hazard Recycler", base_location_id + 107,
    "You can Bank on Batman: Minikit 9 - from Parking Two Cars", base_location_id + 108,
    "You can Bank on Batman: Minikit 10 - from Destroying Five Phone Booths", base_location_id + 109,

    "An Icy Reception: Minikit 1 - on Ledge near Spawn", base_location_id + 110,
    "An Icy Reception: Minikit 2 - Behind Boarded Window on Ledge near Spawn", base_location_id + 111,
    "An Icy Reception: Minikit 3 - in Silver Icecream Stand", base_location_id + 112,
    "An Icy Reception: Minikit 4 - Behind Icecream Truck", base_location_id + 113,
    "An Icy Reception: Minikit 5 - in Alley with Hostage", base_location_id + 114,
    "An Icy Reception: Minikit 6 - in Silver Canisters Above Icecream Cones", base_location_id + 115,
    "An Icy Reception: Minikit 7 - in Female Locked Room", base_location_id + 116,
    "An Icy Reception: Minikit 8 - in Silver Object Behind Toxic Gas", base_location_id + 117,
    "An Icy Reception: Minikit 9 - in Vent with Fan", base_location_id + 118,
    "An Icy Reception: Minikit 10 - in Hypnosis Room", base_location_id + 119,

    "Two-Face Chase: Minikit 1 - from Destroying Three Dumpsters", base_location_id + 120,
    "Two-Face Chase: Minikit 2 - in Manhole Cover", base_location_id + 121,
    "Two-Face Chase: Minikit 3 - from Destroying Southwest Trash Dumpster", base_location_id + 122,
    "Two-Face Chase: Minikit 4 - from Destroying Three Cars", base_location_id + 123,
    "Two-Face Chase: Minikit 5 - from Destroying North Supports", base_location_id + 124,
    "Two-Face Chase: Minikit 6 - from Destroying South Supports", base_location_id + 125,
    "Two-Face Chase: Minikit 7 - from Joker's Van Panel", base_location_id + 126,
    "Two-Face Chase: Minikit 8 - from Harley's Truck Panel", base_location_id + 127,
    "Two-Face Chase: Minikit 9 - in Telephone Booth", base_location_id + 128,
    "Two-Face Chase: Minikit 10 - from Destroying Three Food Carts", base_location_id + 129,

    "A Poisonous Appointment: Minikit 1 - from Destroying All Carrots", base_location_id + 130,
    "A Poisonous Appointment: Minikit 2 - on Top of Trees", base_location_id + 131,
    "A Poisonous Appointment: Minikit 3 - in Heated Greenhouse", base_location_id + 132,
    "A Poisonous Appointment: Minikit 4 - Above Orange Flowers", base_location_id + 133,
    "A Poisonous Appointment: Minikit 5 - by Rail above Potted Plant", base_location_id + 134,
    "A Poisonous Appointment: Minikit 6 - in Underwater Pipe", base_location_id + 135,
    "A Poisonous Appointment: Minikit 7 - in Vat near Second Pitcher Plant", base_location_id + 136,
    "A Poisonous Appointment: Minikit 8 - Destroy 3 Carrots", base_location_id + 137,
    "A Poisonous Appointment: Minikit 9 - Above Heated Pipes", base_location_id + 138,
    "A Poisonous Appointment: Minikit 10 - in Toxic Waste Room", base_location_id + 139,

    "The Face-Off: Minikit 1 - from Jumping on 5 Poles", base_location_id + 140,
    "The Face-Off: Minikit 2 - on Grapple Point to Right of Spawn", base_location_id + 141,
    "The Face-Off: Minikit 3 - from Building Dollar Sign", base_location_id + 142,
    "The Face-Off: Minikit 4 - in Revolving Door", base_location_id + 143,
    "The Face-Off: Minikit 5 - on Roof Above Recycler", base_location_id + 144,
    "The Face-Off: Minikit 6 - in the Toxic Waste Room Pipe", base_location_id + 145,
    "The Face-Off: Minikit 7 - Underneath the Toxic Waste near the Three Platform Bridge", base_location_id + 146,
    "The Face-Off: Minikit 8 - on Right Side of Toxic Waste Room", base_location_id + 147,
    "The Face-Off: Minikit 9 - on Right Side of Vault Room", base_location_id + 148,
    "The Face-Off: Minikit 10 - from Destroying Five Chests", base_location_id + 149,

    "There She Goes Again: Minikit 1 - in Female Locked Room", base_location_id + 150,
    "There She Goes Again: Minikit 2 - from Driving Car Into Garage", base_location_id + 151,
    "There She Goes Again: Minikit 3 - Locked Underwater Behind Fence", base_location_id + 152,
    "There She Goes Again: Minikit 4 - from Destroying Three Carrots", base_location_id + 153,
    "There She Goes Again: Minikit 5 - Locked Underwater by Blue Pump", base_location_id + 154,
    "There She Goes Again: Minikit 6 - from Lawnmowing Flowers", base_location_id + 155,
    "There She Goes Again: Minikit 7 - Behind Window Above Dumpster", base_location_id + 156,
    "There She Goes Again: Minikit 8 - Behind Second Dumpster Under Water Tower", base_location_id + 157,
    "There She Goes Again: Minikit 9 - in Glass Roof", base_location_id + 158,
    "There She Goes Again: Minikit 10 - in Pipe After Breaking Glass", base_location_id + 159,

    "Batboat Battle: Minikit 1 - from Turning on Lighthouse", base_location_id + 160,
    "Batboat Battle: Minikit 2 - from Blowing Up Silver Box", base_location_id + 161,
    "Batboat Battle: Minikit 3 - from Sinking the Ship", base_location_id + 162,
    "Batboat Battle: Minikit 4 - from Pulling the Pipe", base_location_id + 163,
    "Batboat Battle: Minikit 5 - in Alcove that is Surrounded by Ice", base_location_id + 164,
    "Batboat Battle: Minikit 6 - in Silver Crate Surrounded by Toxic Water", base_location_id + 165,
    "Batboat Battle: Minikit 7 - from Destroying Silver Around Pipe", base_location_id + 166,
    "Batboat Battle: Minikit 8 - from Destroying Three Buoys", base_location_id + 167,
    "Batboat Battle: Minikit 9 - in Corner Surrounded by Ice", base_location_id + 168,
    "Batboat Battle: Minikit 10 - from Destroying Three Silver Boxes in Toxic Water", base_location_id + 169,


}

hostage_location_table = {
    "You Can Bank On Batman: Hostage", base_location_id + 400,
    "An Icy Reception: Hostage", base_location_id + 401,
    "A Poisonous Appointment: Hostage", base_location_id + 402,
    "The Face-Off: Hostage", base_location_id + 403,
    "There She Goes Again: Hostage", base_location_id + 404,
    "Under The City: Hostage", base_location_id + 405,
    "Zoo's Company: Hostage", base_location_id + 406,
    "Penguin's Lair: Hostage", base_location_id + 407,
    "Joker's Home Turf: Hostage", base_location_id + 408,
    "Little Fun at the Big Top: Hostage", base_location_id + 409,
    "In the Dark Night: Hostage", base_location_id + 410,
    "To the Top of the Tower: Hostage", base_location_id + 411,
    "The Riddler Makes a Withdrawal: Hostage", base_location_id + 412,
    "On the Rocks: Hostage", base_location_id + 413,
    "Green Fingers: Hostage", base_location_id + 414,
    "An Enterprising Theft: Hostage", base_location_id + 415,
    "Breaking Blocks: Hostage", base_location_id + 416,
    "Rockin' the Docks: Hostage", base_location_id + 417,
    "Stealing the Show: Hostage", base_location_id + 418,
    "A Daring Rescue: Hostage", base_location_id + 419,
    "Arctic World: Hostage", base_location_id + 420,
    "A Surprise for the Commissioner: Hostage", base_location_id + 421,
    "The Joker's Masterpiece: Hostage", base_location_id + 422,
    "The Lure of the Night: Hostage", base_location_id + 423,
    "Dying of Laughter: Hostage", base_location_id + 424,
}

location_table = {
    **minikit_location_table, **hostage_location_table
}
