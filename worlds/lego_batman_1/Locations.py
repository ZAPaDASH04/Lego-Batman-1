from BaseClasses import Location

class LB1Location(Location):
    game: str = "Lego Batman: The Videogame"


base_location_id = 49000000

minikit_location_table = {
    "You can Bank on Batman: Minikit Inside Garage", base_location_id + 100,
    "You can Bank on Batman: Minikit Above Garage", base_location_id + 101,
    "You can Bank on Batman: Minikit Behind Glass Window", base_location_id + 102,
    "You can Bank on Batman: Minikit Mind Control Behind Van", base_location_id + 103,
    "You can Bank on Batman: Minikit in Sewer Grate", base_location_id + 104,
    "You can Bank on Batman: Minikit in High Window", base_location_id + 105,
    "You can Bank on Batman: Minikit on Balcony", base_location_id + 106,
    "You can Bank on Batman: Minikit from Hazard Recycler", base_location_id + 107,
    "You can Bank on Batman: Minikit from Parking Cars", base_location_id + 108,
    "You can Bank on Batman: Minikit from Destroying Phone Booths", base_location_id + 109,

    "An Icy Reception: Minikit on Ledge", base_location_id + 110,
    "An Icy Reception: Minikit Behind Boarded Window on Ledge", base_location_id + 111,
    "An Icy Reception: Minikit in Icecream Stand", base_location_id + 112,
    "An Icy Reception: Minikit Behind Icecream Truck", base_location_id + 113,
    "An Icy Reception: Minikit in Hostage Alley", base_location_id + 114,
    "An Icy Reception: Minikit in Canisters Above Icecream Cones", base_location_id + 115,
    "An Icy Reception: Minikit in Female Locked Room", base_location_id + 116,
    "An Icy Reception: Minikit Behind Toxic Gas", base_location_id + 117,
    "An Icy Reception: Minikit in Vent with Fan", base_location_id + 118,
    "An Icy Reception: Minikit in Hypnosis Room", base_location_id + 119,

    "Two-Face Chase: Minikit from Destroying Three Dumpsters", base_location_id + 120,
    "Two-Face Chase: Minikit in Manhole Cover", base_location_id + 121,
    "Two-Face Chase: Minikit from Destroying One Dumpster", base_location_id + 122,
    "Two-Face Chase: Minikit from Destroying Three Cars", base_location_id + 123,
    "Two-Face Chase: Minikit from Destroying North Supports", base_location_id + 124,
    "Two-Face Chase: Minikit from Destroying South Supports", base_location_id + 125,
    "Two-Face Chase: Minikit from Joker Panel", base_location_id + 126,
    "Two-Face Chase: Minikit from Harley Panel", base_location_id + 127,
    "Two-Face Chase: Minikit in Telephone Booth", base_location_id + 128,
    "Two-Face Chase: Minikit from Destroying Three Food Carts", base_location_id + 129,

    "A Poisonous Appointment: Minikit from Destroying Carrots", base_location_id + 130,
    "A Poisonous Appointment: Minikit on top of Trees", base_location_id + 131,
    "A Poisonous Appointment: Minikit in Heated Greenhouse", base_location_id + 132,
    "A Poisonous Appointment: Minikit Above Orange Flowers", base_location_id + 133,
    "A Poisonous Appointment: Minikit by Rail above Potted Plant", base_location_id + 134,
    "A Poisonous Appointment: Minikit in Pipe", base_location_id + 135,
    "A Poisonous Appointment: Minikit in Vat", base_location_id + 136,
    "A Poisonous Appointment: Minikit Destroy 3 Carrots", base_location_id + 137,
    "A Poisonous Appointment: Minikit Above Heated Pipes", base_location_id + 138,
    "A Poisonous Appointment: Minikit in Toxic Waste Room", base_location_id + 139,

    "The Face-Off: Minikit from Jumping on 5 Poles", base_location_id + 140,
    "The Face-Off: Minikit on Grapple Point", base_location_id + 141,
    "The Face-Off: Minikit from Building Dollar Sign", base_location_id + 142,
    "The Face-Off: Minikit in Revolving Door", base_location_id + 143,
    "The Face-Off: Minikit on Roof Above Recycler", base_location_id + 144,
    "The Face-Off: Minikit in Pipe", base_location_id + 145,
    "The Face-Off: Minikit Underneath the Toxic Waste near the Three Platform Bridge", base_location_id + 146,
    "The Face-Off: Minikit on Right Side of Toxic Waste Room", base_location_id + 147,
    "The Face-Off: Minikit on Right Side of Vault Room", base_location_id + 148,
    "The Face-Off: Minikit from Destroying Five Chests of Money", base_location_id + 149,

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