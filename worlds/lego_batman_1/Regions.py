import typing

from BaseClasses import MultiWorld, Region, Entrance, Location
from .Options import LB1Options
from .Locations import LB1Location, location_table, minikit_location_table


class LB1Region(Region):
    subregions: typing.List[Region] = []


lb1_regions = [
    "Menu",
    "Batcave",
    "Arkham Asylum",
    "Status Screen"
    "You can Bank on Batman",
    # "An Icy Reception",
    # "Two-Face Chase",
    # "A Poisonous Appointment",
    # "The Face-Off",
    # "There She Goes Again",
    # "Batboat Battle"
]


def create_regions(world: MultiWorld, options: LB1Options, player: int):
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    batcave = create_region("Batcave", player, world)
    world.regions.append(batcave)

    arkham_asylum = create_region("Arkham Asylum", player, world)
    world.regions.append(arkham_asylum)

    status_screen = create_region("Status Screen", player, world)
    world.regions.append(status_screen)

    you_can_bank_on_batman = create_region("You can Bank on Batman", player, world)
    world.regions.append(you_can_bank_on_batman)

    connect_regions(world, player, "Menu", "You can Bank on Batman")


    for name in minikit_location_table:
        if name.startswith("You can Bank on Batman"):
            create_location(you_can_bank_on_batman, name)


def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None) -> Entrance:
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    return source_region.connect(target_region, rule=rule)


def create_region(name: str, player: int, world: MultiWorld) -> LB1Region:
    region = LB1Region(name, player, world)
    world.regions.append(region)
    return region


def create_location(reg: Region, *location: str):
    reg.locations += [LB1Location(reg.player, loc_name, location_table[loc_name], reg) for loc_name in location]
