from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Optional, Dict

base_item_id: int = 400000

class LB1Item(Item):
    game: str = "Lego Batman: The Video Game"

class LB1ItemData(NamedTuple):
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.progression_skip_balancing

#TODO: add in progression classification based off of win con (look at manual's implementation - need to decide win cons first)
minikit_item_table: Dict[str, LB1ItemData] = {
    "You can Bank on Batman: Minikit 1": LB1ItemData(base_item_id + 100),
    "You can Bank on Batman: Minikit 2": LB1ItemData(base_item_id + 101),
    "You can Bank on Batman: Minikit 3": LB1ItemData(base_item_id + 102),
    "You can Bank on Batman: Minikit 4": LB1ItemData(base_item_id + 103),
    "You can Bank on Batman: Minikit 5": LB1ItemData(base_item_id + 104),
    "You can Bank on Batman: Minikit 6": LB1ItemData(base_item_id + 105),
    "You can Bank on Batman: Minikit 7": LB1ItemData(base_item_id + 106),
    "You can Bank on Batman: Minikit 8": LB1ItemData(base_item_id + 107),
    "You can Bank on Batman: Minikit 9": LB1ItemData(base_item_id + 108),
    "You can Bank on Batman: Minikit 10": LB1ItemData(base_item_id + 109),
    
    "An Icy Reception: Minikit 1": LB1ItemData(base_item_id + 110),
    "An Icy Reception: Minikit 2": LB1ItemData(base_item_id + 111),
    "An Icy Reception: Minikit 3": LB1ItemData(base_item_id + 112),
    "An Icy Reception: Minikit 4": LB1ItemData(base_item_id + 113),
    "An Icy Reception: Minikit 5": LB1ItemData(base_item_id + 114),
    "An Icy Reception: Minikit 6": LB1ItemData(base_item_id + 115),
    "An Icy Reception: Minikit 7": LB1ItemData(base_item_id + 116),
    "An Icy Reception: Minikit 8": LB1ItemData(base_item_id + 117),
    "An Icy Reception: Minikit 9": LB1ItemData(base_item_id + 118),
    "An Icy Reception: Minikit 10": LB1ItemData(base_item_id + 119),

    "Two-Face Chase: Minikit 1": LB1ItemData(base_item_id + 120),
    "Two-Face Chase: Minikit 2": LB1ItemData(base_item_id + 121),
    "Two-Face Chase: Minikit 3": LB1ItemData(base_item_id + 122),
    "Two-Face Chase: Minikit 4": LB1ItemData(base_item_id + 123),
    "Two-Face Chase: Minikit 5": LB1ItemData(base_item_id + 124),
    "Two-Face Chase: Minikit 6": LB1ItemData(base_item_id + 125),
    "Two-Face Chase: Minikit 7": LB1ItemData(base_item_id + 126),
    "Two-Face Chase: Minikit 8": LB1ItemData(base_item_id + 127),
    "Two-Face Chase: Minikit 9": LB1ItemData(base_item_id + 128),
    "Two-Face Chase: Minikit 10": LB1ItemData(base_item_id + 129),

    "A Poisonous Appointment: Minikit 1": LB1ItemData(base_item_id + 130),
    "A Poisonous Appointment: Minikit 2": LB1ItemData(base_item_id + 131),
    "A Poisonous Appointment: Minikit 3": LB1ItemData(base_item_id + 132),
    "A Poisonous Appointment: Minikit 4": LB1ItemData(base_item_id + 133),
    "A Poisonous Appointment: Minikit 5": LB1ItemData(base_item_id + 134),
    "A Poisonous Appointment: Minikit 6": LB1ItemData(base_item_id + 135),
    "A Poisonous Appointment: Minikit 7": LB1ItemData(base_item_id + 136),
    "A Poisonous Appointment: Minikit 8": LB1ItemData(base_item_id + 137),
    "A Poisonous Appointment: Minikit 9": LB1ItemData(base_item_id + 138),
    "A Poisonous Appointment: Minikit 10": LB1ItemData(base_item_id + 139),

    "The Face-Off: Minikit 1": LB1ItemData(base_item_id + 140),
    "The Face-Off: Minikit 2": LB1ItemData(base_item_id + 141),
    "The Face-Off: Minikit 3": LB1ItemData(base_item_id + 142),
    "The Face-Off: Minikit 4": LB1ItemData(base_item_id + 143),
    "The Face-Off: Minikit 5": LB1ItemData(base_item_id + 144),
    "The Face-Off: Minikit 6": LB1ItemData(base_item_id + 145),
    "The Face-Off: Minikit 7": LB1ItemData(base_item_id + 146),
    "The Face-Off: Minikit 8": LB1ItemData(base_item_id + 147),
    "The Face-Off: Minikit 9": LB1ItemData(base_item_id + 148),
    "The Face-Off: Minikit 10": LB1ItemData(base_item_id + 149),
    #
    # "There She Goes Again: Minikit 1": LB1ItemData(base_item_id + 150),
    # "There She Goes Again: Minikit 2": LB1ItemData(base_item_id + 151),
    # "There She Goes Again: Minikit 3": LB1ItemData(base_item_id + 152),
    # "There She Goes Again: Minikit 4": LB1ItemData(base_item_id + 153),
    # "There She Goes Again: Minikit 5": LB1ItemData(base_item_id + 154),
    # "There She Goes Again: Minikit 6": LB1ItemData(base_item_id + 155),
    # "There She Goes Again: Minikit 7": LB1ItemData(base_item_id + 156),
    # "There She Goes Again: Minikit 8": LB1ItemData(base_item_id + 157),
    # "There She Goes Again: Minikit 9": LB1ItemData(base_item_id + 158),
    # "There She Goes Again: Minikit 10": LB1ItemData(base_item_id + 159),
    #
    # "Batboat Battle: Minikit 1": LB1ItemData(base_item_id + 160),
    # "Batboat Battle: Minikit 2": LB1ItemData(base_item_id + 161),
    # "Batboat Battle: Minikit 3": LB1ItemData(base_item_id + 162),
    # "Batboat Battle: Minikit 4": LB1ItemData(base_item_id + 163),
    # "Batboat Battle: Minikit 5": LB1ItemData(base_item_id + 164),
    # "Batboat Battle: Minikit 6": LB1ItemData(base_item_id + 165),
    # "Batboat Battle: Minikit 7": LB1ItemData(base_item_id + 166),
    # "Batboat Battle: Minikit 8": LB1ItemData(base_item_id + 167),
    # "Batboat Battle: Minikit 9": LB1ItemData(base_item_id + 168),
    # "Batboat Battle: Minikit 10": LB1ItemData(base_item_id + 169),
    
}

# hostage_item_table: Dict[str, LB1ItemData] = {
#     "You Can Bank On Batman: Hostage": LB1ItemData(base_item_id + 400),
#     # "An Icy Reception: Hostage": LB1ItemData(base_item_id + 401),
#     # "A Poisonous Appointment: Hostage": LB1ItemData(base_item_id + 402),
#     # "The Face-Off: Hostage": LB1ItemData(base_item_id + 403),
#     # "There She Goes Again: Hostage": LB1ItemData(base_item_id + 404),
#     # "Under The City: Hostage": LB1ItemData(base_item_id + 405),
#     # "Zoo's Company: Hostage": LB1ItemData(base_item_id + 406),
#     # "Penguin's Lair: Hostage": LB1ItemData(base_item_id + 407),
#     # "Joker's Home Turf: Hostage": LB1ItemData(base_item_id + 408),
#     # "Little Fun at the Big Top: Hostage": LB1ItemData(base_item_id + 409),
#     # "In the Dark Night: Hostage": LB1ItemData(base_item_id + 410),
#     # "To the Top of the Tower: Hostage": LB1ItemData(base_item_id + 411),
#     # "The Riddler Makes a Withdrawal: Hostage": LB1ItemData(base_item_id + 412),
#     # "On the Rocks: Hostage": LB1ItemData(base_item_id + 413),
#     # "Green Fingers: Hostage": LB1ItemData(base_item_id + 414),
#     # "An Enterprising Theft: Hostage": LB1ItemData(base_item_id + 415),
#     # "Breaking Blocks: Hostage": LB1ItemData(base_item_id + 416),
#     # "Rockin' the Docks: Hostage": LB1ItemData(base_item_id + 417),
#     # "Stealing the Show: Hostage": LB1ItemData(base_item_id + 418),
#     # "A Daring Rescue: Hostage": LB1ItemData(base_item_id + 419),
#     # "Arctic World: Hostage": LB1ItemData(base_item_id + 420),
#     # "A Surprise for the Commissioner: Hostage": LB1ItemData(base_item_id + 421),
#     # "The Joker's Masterpiece: Hostage": LB1ItemData(base_item_id + 422),
#     # "The Lure of the Night: Hostage": LB1ItemData(base_item_id + 423),
#     # "Dying of Laughter: Hostage": LB1ItemData(base_item_id + 424),
# }

item_data_table = {
    **minikit_item_table,
    # **hostage_item_table,
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}

event_item_table: Dict[str, LB1ItemData] = {
    # "Completed Wayne Manor": LB1ItemData(None, classification=ItemClassification.progression),
    # "Completed Arkham Asylum": LB1ItemData(None, classification=ItemClassification.progression),
    # "Completed All Levels": LB1ItemData(None, classification=ItemClassification.progression),
    "Obtain All Minikits": LB1ItemData(None, classification=ItemClassification.progression),
    # "Hush": LB1ItemData(None, classification=ItemClassification.progression),
    # "Ra Sha Guul": LB1ItemData(None, classification=ItemClassification.progression),
}



