from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Optional, TypedDict, Dict


class LegoBatman1temData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1

def get_items_by_category(category: str) -> Dict[str, LegoBatman1ItemData]: 
    return {name: data for name, data in item_table.items() if data.category == category}

class LegoBatman1Item(Item):
    game: str = "Lego Batman: The Video Game"


item_table: Dict[str, LegoBatman1ItemData] = {

}

hostagesanity_item = {
    #Hostages 
    "Hostage":                             LegoBatman1ItemData("Hostage",    450359962127, if self.options.hush or self.options.ra_sha_guul: ItemClassification.progression_skip_balancing else ItemClassification.useful,25),
}

kitsanity_item = {
    #Kits
    "Mini-Kit":                             LegoBatman1ItemData("Mini-Kit",    45035996200, if self.options.kits or self.options.ra_sha_guul: ItemClassification.progression_skip_balancing else ItemClassification.useful,300),
}



event_item_table: Dict[str, LegoBatman1ItemData] = {
    "Completed All Levels":     LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Completed Arkham Asylum":  LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Completed Wayne Mannor":   LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Ra Sha Guul":              LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Hush":                     LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "100% Obtained":            LegoBatman1ItemData("Event", classification=ItemClassification.progression),
}

def get_items(world):
    item_table = basic_item.copy()
    
    if world.options.char_shop_sanity:
        item_table.update(charshopsanity_item)

    if world.options.hostage_sanity:
        item_table.update(hostagesanity_item)

    if world.options.kit_sanity:
        item_table.update(kitsanity_item)
    
    return item_table