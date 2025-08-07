
# world/lego_batman_1/__init__.py

import settings
import typing
from .Options import LegoBatman1Options  # the options we defined earlier
from .Items import LegoBatman1_items  # data used below to add items to the World
from .Locations import LegoBatman1_locations  # same as above
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification


class LegoBatman1Item(Item):  # or from Items import LegoBatman1Item
    game = "My Game"  # name of the game/world this item is from


class LegoBatman1Location(Location):  # or from Locations import LegoBatman1Location
    game = "My Game"  # name of the game/world this location is in

class LegoBatman1Web(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Lego Batman: The Videogame integration for Archipelago multiworld games.",
        "English",
        "LegoBatman1_setup_en.md",
        "LegoBatman1_setup/en",
        ["ZAPaDASH04"]
    )]

# class LegoBatman1Settings(settings.Group):
#     class RomFile(settings.SNESRomPath):
#         """Insert help text for host.yaml here."""

#     rom_file: RomFile = RomFile("MyGame.sfc")


class LegoBatman1World(World):
    """
     When all the villains in Arkham Asylum team up and break loose, only the dynamic duo is bold enough to take them on to save Gotham City. 
     The fun of LEGO, the drama of Batman and the uniqueness of the combination makes for a comical and exciting adventure in LEGO Batman: The Videogame. 
    """ # from steam
    game = "Lego Batman: The Videogame"
    options_dataclass = LegoBatman1Options  # options the player can set
    options: LegoBatman1Options  # typing hints for option results
    settings: typing.ClassVar[LegoBatman1Settings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: id for
                       id, name in enumerate(LegoBatman1_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(LegoBatman1_locations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "weapons": {"sword", "lance"},
    }


# import string

# from .items import LegoBatman1Item, item_table, item_pool_weights, offset, filler_table
# from .locations import LegoBatman1Location
# from .rules import set_rules

# from BaseClasses import Item, ItemClassification, Tutorial
# from .options import ItemWeights, LegoBatman1Options
# from worlds.AutoWorld import World, WebWorld
# from .regions 
# from typing import List, Dict, Any


# class LegoBatman1(WebWorld):
#     theme = "stone"
#     tutorials = [Tutorial(
#         "Multiworld Setup Guide",
#         "A guide to setting up the Lego Batman The Videogame integration for Archipelago multiworld games.",
#         "English",
#         "setup_en.md",
#         "setup/en",
#         ["Ijwu", "Kindasneaki"]
#     )]


# class LegoBatman1World(World):
#     """
#      When all the villains in Arkham Asylum team up and break loose, only the dynamic duo is bold enough to take them on to save Gotham City. 
#      The fun of LEGO, the drama of Batman and the uniqueness of the combination makes for a comical and exciting adventure in LEGO Batman: The Videogame. 
#     """ #Lazy Import
#     game = "Lego Batman: The Video Game"
#     options_dataclass = LegoBatman1Options
#     options: LegoBatman1Options
#     topology_present = True

#     item_name_to_id = {name: data.code for name, data in item_table.items()}
#     location_name_to_id = {name: data.code for name, data in location_table.items()}

    
#     item_name_groups = {
#         # clayface mrfreeze poisonivy twoface riddler
#         # bane catwoman+catwoman2 killercroc manbat penguin
#         # harleyquinn scarecrow killermoth madhatter joker+jokerhawaiian
#         "batman": {"batman","batgirl"},
#         "robin": {"robin","nightwing"},
#         "batarang": {"batman","robin","batgirl","nightwing"},
#         "grapple": {"batman","robin","batgirl","nightwing"},
#         # "gun": {},
#         "toxic": {"biohazardscientist","mrfreeze","poisonivy","twoface","bane","killercroc","joker","jokerhawaiian"},
#         "strong": {"clayface","mrfreeze","bane","killercroc","manbat"},
#         "doublejump": {"clayface","poisonivy", "catwoman", "catwoman2", "madhatter"},
#         "hypnosis": {"riddler","scarecrow","madhatter"}, # hypnosis + security_access "NoDoor" (questionmarks)
#         "femininewiles": {"poisonivy","catwoman","harleyquinn"}, # security_access "LoveHearts"
#         "tightrope": {"robin","brucewayne","alfred","batgirl","nightwing","commissionergordon","policeman_2","fish_monger","military_policeman","securityguard_1","swatteam"},
#         "explosive": {"suit_demolition","penguin"},
#         "glide": {"suit_glide", "manbat", "killermoth", "penguin"},
#         "sink": {"suit_scuba", "killercroc"},
#         # unique abilities
#         "mrfreeze": {"mrfreeze"},
#         "poisonivy": {"poisonivy"},
#     }

#     data_version = 1
#     required_client_version = (0, 4, 4)
#     web = LegoBatman1Web()
   