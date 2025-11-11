from BaseClasses import MultiWorld, Region, Entrance, Location, ItemClassification
from .Locations import LB1Location, event_location_table
from .Items import LB1Item
from .Names import RegionName


lb1_hub_regions = [
    RegionName.bc,
    RegionName.aa,
    RegionName.sh,
]

lb1_hero_regions = [
    RegionName.ycbob,
    RegionName.air,
    RegionName.tfc,
    RegionName.apa,
    RegionName.tfo,
    RegionName.tsga,
    RegionName.bbb,
    RegionName.utc,
    RegionName.zc,
    RegionName.pl,
    RegionName.jht,
    RegionName.lfabt,
    RegionName.fotb,
    RegionName.itdn,
    RegionName.tttot,
]

lb1_villain_regions = [
    RegionName.trmaw,
    RegionName.otr,
    RegionName.gf,
    RegionName.aet,
    RegionName.bb,
    RegionName.rtd,
    RegionName.sts,
    RegionName.hag,
    RegionName.adr,
    RegionName.aw,
    RegionName.asftc,
    RegionName.bbpl,
    RegionName.tjm,
    RegionName.tlotn,
    RegionName.dol,
]

lb1_hero_subregions = [
    RegionName.ycbobf,
    RegionName.airf,
    RegionName.tfcf,
    RegionName.apaf,
    RegionName.tfof,
    RegionName.tsgaf,
    RegionName.bbbf,
    RegionName.utcf,
    RegionName.zcf,
    RegionName.plf,
    # RegionName.jhtf,
    RegionName.lfabtf,
    # RegionName.fotbf,
    RegionName.itdnf,
    RegionName.tttotf,
]

lb1_villain_subregions = [
    RegionName.trmawf,
    RegionName.otrf,
    RegionName.gff,
    # RegionName.aetf,
    RegionName.bbf,
    RegionName.rtdf,
    RegionName.stsf,
    RegionName.hagf,
    RegionName.adrf,
    RegionName.awf,
    RegionName.asftcf,
    RegionName.bbplf,
    RegionName.tjmf,
    RegionName.tlotnf,
    RegionName.dolf,
]

lb1_all_regions = [
    *lb1_hub_regions,
    *lb1_hero_regions,
    *lb1_villain_regions,
    *lb1_hero_subregions,
    *lb1_villain_subregions,
]


def create_regions(world: MultiWorld, player: int, seed_locations):
    menu = Region("Menu", player, world)
    world.regions.append(menu)

    for region in lb1_all_regions:
        create_regions_and_locations(region, player, world, seed_locations)

    connect_regions(world, player, "Menu", RegionName.bc)
    connect_regions(world, player, RegionName.bc, RegionName.aa)
    connect_regions(world, player, RegionName.bc, RegionName.sh)

    for region in lb1_hero_regions:
        connect_regions(world, player, RegionName.bc, region)

    for region in lb1_villain_regions:
        connect_regions(world, player, RegionName.aa, region)

    connect_regions(world, player, RegionName.ycbob, RegionName.ycbobf)
    connect_regions(world, player, RegionName.air, RegionName.airf)
    connect_regions(world, player, RegionName.tfc, RegionName.tfcf)
    connect_regions(world, player, RegionName.apa, RegionName.apaf)
    connect_regions(world, player, RegionName.tfo, RegionName.tfof)
    connect_regions(world, player, RegionName.tsga, RegionName.tsgaf)
    connect_regions(world, player, RegionName.bbb, RegionName.bbbf)
    connect_regions(world, player, RegionName.utc, RegionName.utcf)
    connect_regions(world, player, RegionName.zc, RegionName.zcf)
    connect_regions(world, player, RegionName.pl, RegionName.plf)
    connect_regions(world, player, RegionName.lfabt, RegionName.lfabtf)
    connect_regions(world, player, RegionName.itdn, RegionName.itdnf)
    connect_regions(world, player, RegionName.tttot, RegionName.tttotf)

    connect_regions(world, player, RegionName.trmaw, RegionName.trmawf)
    connect_regions(world, player, RegionName.otr, RegionName.otrf)
    connect_regions(world, player, RegionName.gf, RegionName.gff)
    connect_regions(world, player, RegionName.bb, RegionName.bbf)
    connect_regions(world, player, RegionName.rtd, RegionName.rtdf)
    connect_regions(world, player, RegionName.sts, RegionName.stsf)
    connect_regions(world, player, RegionName.hag, RegionName.hagf)
    connect_regions(world, player, RegionName.adr, RegionName.adrf)
    connect_regions(world, player, RegionName.aw, RegionName.awf)
    connect_regions(world, player, RegionName.asftc, RegionName.asftcf)
    connect_regions(world, player, RegionName.bbpl, RegionName.bbplf)
    connect_regions(world, player, RegionName.tjm, RegionName.tjmf)
    connect_regions(world, player, RegionName.tlotn, RegionName.tlotnf)
    connect_regions(world, player, RegionName.dol, RegionName.dolf)


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

    for (name, data) in event_location_table.items():
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
