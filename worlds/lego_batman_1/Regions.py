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
    "There She Goes Again",
    "Batboat Battle",
    "Under the City",
    "Zoo's Company",
    "Penguin's Lair",
    "Joker's Home Turf",
    "Little Fun at Big Top",
    "Flight of the Bat",
    "In the Dark Night",
    "To the Top of the Tower"
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

    there_she_goes_again = create_region("There She Goes Again", player, world)
    world.regions.append(there_she_goes_again)

    batboat_battle = create_region("Batboat Battle", player, world)
    world.regions.append(batboat_battle)

    under_the_city = create_region("Under the City", player, world)
    world.regions.append(under_the_city)

    zoos_company = create_region("Zoo's Company", player, world)
    world.regions.append(zoos_company)

    penguins_lair = create_region("Penguin's Lair", player, world)
    world.regions.append(penguins_lair)

    jokers_home_turf = create_region("Joker's Home Turf", player, world)
    world.regions.append(jokers_home_turf)

    little_fun_at_big_top = create_region("Little Fun at Big Top", player, world)
    world.regions.append(little_fun_at_big_top)

    flight_of_the_bat = create_region("Flight of the Bat", player, world)
    world.regions.append(flight_of_the_bat)

    in_the_dark_night = create_region("In the Dark Night", player, world)
    world.regions.append(in_the_dark_night)

    to_the_top_of_the_tower = create_region("To the Top of the Tower", player, world)
    world.regions.append(to_the_top_of_the_tower)

    connect_regions(world, player, "Menu", "Batcave")
    connect_regions(world, player, "Batcave", "Arkham Asylum")
    connect_regions(world, player, "Batcave", "You can Bank on Batman")
    connect_regions(world, player, "Batcave", "An Icy Reception")
    connect_regions(world, player, "Batcave", "Two-Face Chase")
    connect_regions(world, player, "Batcave", "A Poisonous Appointment")
    connect_regions(world, player, "Batcave", "The Face-Off")
    connect_regions(world, player, "Batcave", "There She Goes Again")
    connect_regions(world, player, "Batcave", "Batboat Battle")
    connect_regions(world, player, "Batcave", "Under the City")
    connect_regions(world, player, "Batcave", "Zoo's Company")
    connect_regions(world, player, "Batcave", "Penguin's Lair")
    connect_regions(world, player, "Batcave", "Joker's Home Turf")
    connect_regions(world, player, "Batcave", "Little Fun at Big Top")
    connect_regions(world, player, "Batcave", "Flight of the Bat")
    connect_regions(world, player, "Batcave", "In the Dark Night")
    connect_regions(world, player, "Batcave", "To the Top of the Tower")

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
        elif name.startswith("There She Goes Again"):
            create_location(there_she_goes_again, name)
        elif name.startswith("Batboat Battle"):
            create_location(batboat_battle, name)
        elif name.startswith("Under the City"):
            create_location(under_the_city, name)
        elif name.startswith("Zoo's Company"):
            create_location(zoos_company, name)
        elif name.startswith("Penguin's Lair"):
            create_location(penguins_lair, name)
        elif name.startswith("Joker's Home Turf"):
            create_location(jokers_home_turf, name)
        elif name.startswith("Little Fun at Big Top"):
            create_location(little_fun_at_big_top, name)
        elif name.startswith("Flight of the Bat"):
            create_location(flight_of_the_bat, name)
        elif name.startswith("In the Dark Night"):
            create_location(in_the_dark_night, name)
        elif name.startswith("To the Top of the Tower"):
            create_location(to_the_top_of_the_tower, name)

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
