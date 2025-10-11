from BaseClasses import MultiWorld, Region, Entrance, Location, ItemClassification
from .Locations import LB1Location, level_beaten_event_location_table
from .Items import LB1Item


lb1_hub_regions = [
    "Batcave",
    "Arkham Asylum",
    "Shop"
]

lb1_hero_regions = [
    "You can Bank on Batman",
    "An Icy Reception",
    "Two-Face Chase",
    "A Poisonous Appointment",
    "The Face-Off",
    "There She Goes Again",
    "Batboat Battle",
    "Under the City",
    "Zoo's Company",
    "Penguin's Lair",
    "Joker's Home Turf",
    "Little Fun at the Big Top",
    "Flight of the Bat",
    "In the Dark Night",
    "To the Top of the Tower",
]

lb1_villain_regions = [
    "The Riddler Makes a Withdrawal",
    "On the Rocks",
    "Green Fingers",
    "An Enterprising Theft",
    "Breaking Blocks",
    "Rockin' the Docks",
    "Stealing the Show",
    "Harbouring a Grudge",
    "A Daring Rescue",
    "Arctic World",
    "A Surprise for the Commissioner",
    "Biplane Blast",
    "The Joker's Masterpiece",
    "The Lure of the Night",
    "Dying of Laughter",
]

lb1_villain_subregions = [
    "You can Bank on Batman: Freeplay",
    "An Icy Reception: Freeplay",
    "Two-Face Chase: Freeplay",
    "There She Goes Again: Freeplay",
    "The Riddler Makes a Withdrawal: Freeplay",
    "On the Rocks: Freeplay",
    "Green Fingers: Freeplay",
    "Breaking Blocks: Freeplay",
    "Rockin' the Docks: Freeplay",
    "Stealing the Show: Freeplay",
    "Harbouring a Grudge: Freeplay",
    "A Daring Rescue: Freeplay",
    "Arctic World: Freeplay",
    "A Surprise for the Commissioner: Freeplay",
    "Biplane Blast: Freeplay",
    "The Joker's Masterpiece: Freeplay",
    "The Lure of the Night: Freeplay",
    "Dying of Laughter: Freeplay",
]

lb1_all_regions = [
    *lb1_hub_regions,
    *lb1_hero_regions,
    *lb1_villain_regions,
    *lb1_villain_subregions,
]


def create_regions(world: MultiWorld, player: int, seed_locations):
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    for region in lb1_all_regions:
        create_regions_and_locations(region, player, world, seed_locations)

    connect_regions(world, player, "Menu", "Batcave")
    connect_regions(world, player, "Batcave", "Arkham Asylum")
    connect_regions(world, player, "Batcave", "Shop")

    for region in lb1_hero_regions:
        connect_regions(world, player, "Batcave", region)

    for region in lb1_villain_regions:
        connect_regions(world, player, "Arkham Asylum", region)

    connect_regions(world, player, "You can Bank on Batman", "You can Bank on Batman: Freeplay")
    connect_regions(world, player, "An Icy Reception", "An Icy Reception: Freeplay")
    connect_regions(world, player, "Two-Face Chase", "Two-Face Chase: Freeplay")
    connect_regions(world, player, "There She Goes Again", "There She Goes Again: Freeplay")

    connect_regions(world, player, "The Riddler Makes a Withdrawal", "The Riddler Makes a Withdrawal: Freeplay")
    connect_regions(world, player, "On the Rocks", "On the Rocks: Freeplay")
    connect_regions(world, player, "Green Fingers", "Green Fingers: Freeplay")
    connect_regions(world, player, "Breaking Blocks", "Breaking Blocks: Freeplay")
    connect_regions(world, player, "Rockin' the Docks", "Rockin' the Docks: Freeplay")
    connect_regions(world, player, "Stealing the Show", "Stealing the Show: Freeplay")
    connect_regions(world, player, "Harbouring a Grudge", "Harbouring a Grudge: Freeplay")
    connect_regions(world, player, "A Daring Rescue", "A Daring Rescue: Freeplay")
    connect_regions(world, player, "Arctic World", "Arctic World: Freeplay")
    connect_regions(world, player, "A Surprise for the Commissioner", "A Surprise for the Commissioner: Freeplay")
    connect_regions(world, player, "Biplane Blast", "Biplane Blast: Freeplay")
    connect_regions(world, player, "The Joker's Masterpiece", "The Joker's Masterpiece: Freeplay")
    connect_regions(world, player, "The Lure of the Night", "The Lure of the Night: Freeplay")
    connect_regions(world, player, "Dying of Laughter", "Dying of Laughter: Freeplay")


def connect_regions(world: MultiWorld, player: int, source: str, target: str) -> Entrance:
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    return source_region.connect(target_region)


def create_regions_and_locations(name: str, player: int, world: MultiWorld, seed_locations) -> Region:
    region = Region(name, player, world)

    for (key, data) in seed_locations.items():
        if data.region == name:
            location = LB1Location(player, key, data.id, region)
            region.locations.append(location)

    world.regions.append(region)
    return region


def create_events(world: MultiWorld, player: int) -> int:
    count = 0

    for (name, data) in level_beaten_event_location_table.items():
        item_name = "Level Beaten Token"
        event: Location = create_event(name, item_name, world.get_region(data.region, player), player)
        event.show_in_spoiler = True
        count += 1

    return count


def create_event(name: str, item_name: str, region: Region, player: int) -> Location:
    event = LB1Location(player, name, None, region)
    region.locations.append(event)
    event.place_locked_item(LB1Item(item_name, ItemClassification.progression, None, player))
    return event
