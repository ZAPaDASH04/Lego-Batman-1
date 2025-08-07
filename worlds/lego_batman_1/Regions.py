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
    "You can Bank on Batman",
    "An Icy Reception",
    "Two-Face Chase",
    "A Poisonous Appointment",
    "The Face-Off",
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

    you_can_bank_on_batman = create_region("You can Bank on Batman", player, world)
    world.regions.append(you_can_bank_on_batman)

    an_icy_reception = create_region("An Icy Reception", player, world)
    world.regions.append(an_icy_reception)

    two_face_chase = create_region("Two-Face Chase", player, world)
    world.regions.append(two_face_chase)

    a_poisonous_appointment = create_region("A Poisonous Appointment", player, world)
    world.regions.append(a_poisonous_appointment)

    the_face_off = create_region("The Face-Off", player, world)
    world.regions.append(the_face_off)

    connect_regions(world, player, "Menu", "Batcave")
    connect_regions(world, player, "Batcave", "Arkham Asylum")
    connect_regions(world, player, "Batcave", "You can Bank on Batman")
    connect_regions(world, player, "Batcave", "An Icy Reception")
    connect_regions(world, player, "Batcave", "Two-Face Chase")
    connect_regions(world, player, "Batcave", "A Poisonous Appointment")
    connect_regions(world, player, "Batcave", "The Face-Off")


    for name in location_table:
        if name.startswith("You can Bank on Batman"):
            create_location(you_can_bank_on_batman, name)
        elif name.startswith("An Icy Reception"):
            create_location(an_icy_reception, name)
        elif name.startswith("Two-Face Chase"):
            create_location(two_face_chase, name)
        elif name.startswith("A Poisonous Appointment"):
            create_location(a_poisonous_appointment, name)
        elif name.startswith("The Face-Off"):
            create_location(the_face_off, name)


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
