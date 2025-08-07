from typing import List, Dict, Any

from BaseClasses import Item, ItemClassification, Tutorial, Region, MultiWorld
from ..AutoWorld import World, WebWorld

from .Items import LB1Item, item_table, item_data_table, minikit_item_table
from .Locations import location_table, LB1Location
from .Options import LB1Options
from .Regions import create_regions, connect_regions, LB1Region
# from .Rules import set_rules

class LB1Web(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Lego Batman: The Videogame for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ZAPaDASH04", "jrad", "Snolid Ice"]
    )]


class LB1World(World):
    """
     When all the villains in Arkham Asylum team up and break loose, only the dynamic duo is bold enough to take them on to save Gotham City. 
     The fun of LEGO, the drama of Batman and the uniqueness of the combination makes for a comical and exciting adventure in LEGO Batman: The Videogame. 
    """ #Lazy Import
    game = "Lego Batman: The Video Game"
    options_dataclass = LB1Options
    options: LB1Options
    topology_present = False

    item_name_to_id = item_table
    location_name_to_id = location_table

    data_version = 1
    required_client_version = (0, 4, 4)
    web = LB1Web()

    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = LB1Item(name, data.classification, data.code, self.player)
        return item

    def create_items(self):
        self.multiworld.itempool += [self.create_item(item_name) for item_name in item_table]