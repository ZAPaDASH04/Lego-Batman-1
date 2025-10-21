from typing import Dict

from BaseClasses import Item, Tutorial
from Options import OptionError
from .Items import LB1Item, item_data_table, minikit_names_set, setup_items, item_group_table
from .Locations import all_location_table, LocationData, setup_locations
from .Names import ItemName, RegionName
from .Options import LB1Options
from .Regions import create_regions, connect_regions, create_events
from .Rules import set_rules, set_event_rules
from ..AutoWorld import World, WebWorld, CollectionState


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
    """
    game = "Lego Batman: The Video Game"
    options_dataclass = LB1Options
    options: LB1Options
    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_data_table.items() if data.code is not None}
    location_name_to_id = {name: data.id for name, data in all_location_table.items()}

    seed_location_table: Dict[str, int]
    seed_item_table: Dict[str, int]

    data_version = 1
    required_client_version = (0, 5, 1)
    web = LB1Web()

    item_name_groups = {
        "Character": item_group_table["character"],
        # "Hard Character": item_group_table["hard character"],
        "Automobile": item_group_table["automobile"],
        "Watercraft": item_group_table["watercraft"],
        "Aircraft": item_group_table["aircraft"],
        "Suit": item_group_table["suit"],
        "Minikit": item_group_table["minikit"],
        "Hostage": item_group_table["hostage"],
        "Level": item_group_table["level"],
        "True Status": item_group_table["true status"],
        "Red Brick Collected": item_group_table["red brick collected"],
        "Red Brick Unlocked": item_group_table["red brick unlocked"],
        "Character Token": item_group_table["character token"],
    }

    location_name_groups = {
        RegionName.ycbob: {name for name, data in all_location_table.items()
                           if data.region == RegionName.ycbob or data.region == RegionName.ycbobf},
        RegionName.air: {name for name, data in all_location_table.items()
                         if data.region == RegionName.air or data.region == RegionName.airf},
        RegionName.tfc: {name for name, data in all_location_table.items()
                         if data.region == RegionName.tfc or data.region == RegionName.tfcf},
        RegionName.apa: {name for name, data in all_location_table.items()
                         if data.region == RegionName.apa or data.region == RegionName.apaf},
        RegionName.tfo: {name for name, data in all_location_table.items()
                         if data.region == RegionName.tfo or data.region == RegionName.tfof},
        RegionName.tsga: {name for name, data in all_location_table.items()
                          if data.region == RegionName.tsga or data.region == RegionName.tsgaf},
        RegionName.bbb: {name for name, data in all_location_table.items()
                         if data.region == RegionName.bbb or data.region == RegionName.bbbf},
        RegionName.utc: {name for name, data in all_location_table.items()
                         if data.region == RegionName.utc or data.region == RegionName.utcf},
        RegionName.zc: {name for name, data in all_location_table.items()
                        if data.region == RegionName.zc or data.region == RegionName.zcf},
        RegionName.pl: {name for name, data in all_location_table.items()
                        if data.region == RegionName.pl or data.region == RegionName.plf},
        RegionName.jht: {name for name, data in all_location_table.items()
                         if data.region == RegionName.jht or data.region == RegionName.jhtf},
        RegionName.lfabt: {name for name, data in all_location_table.items()
                           if data.region == RegionName.lfabt or data.region == RegionName.lfabtf},
        RegionName.fotb: {name for name, data in all_location_table.items()
                          if data.region == RegionName.fotb or data.region == RegionName.fotbf},
        RegionName.itdn: {name for name, data in all_location_table.items()
                          if data.region == RegionName.itdn or data.region == RegionName.itdnf},
        RegionName.tttot: {name for name, data in all_location_table.items()
                           if data.region == RegionName.tttot or data.region == RegionName.tttotf},
        RegionName.trmaw: {name for name, data in all_location_table.items()
                           if data.region == RegionName.trmaw or data.region == RegionName.trmawf},
        RegionName.otr: {name for name, data in all_location_table.items()
                         if data.region == RegionName.otr or data.region == RegionName.otrf},
        RegionName.gf: {name for name, data in all_location_table.items()
                        if data.region == RegionName.gf or data.region == RegionName.gff},
        RegionName.aet: {name for name, data in all_location_table.items()
                         if data.region == RegionName.aet or data.region == RegionName.aetf},
        RegionName.bb: {name for name, data in all_location_table.items()
                        if data.region == RegionName.bb or data.region == RegionName.bbf},
        RegionName.rtd: {name for name, data in all_location_table.items()
                         if data.region == RegionName.rtd or data.region == RegionName.rtdf},
        RegionName.sts: {name for name, data in all_location_table.items()
                         if data.region == RegionName.sts or data.region == RegionName.stsf},
        RegionName.hag: {name for name, data in all_location_table.items()
                         if data.region == RegionName.hag or data.region == RegionName.hagf},
        RegionName.adr: {name for name, data in all_location_table.items()
                         if data.region == RegionName.adr or data.region == RegionName.adrf},
        RegionName.aw: {name for name, data in all_location_table.items()
                        if data.region == RegionName.aw or data.region == RegionName.awf},
        RegionName.asftc: {name for name, data in all_location_table.items()
                           if data.region == RegionName.asftc or data.region == RegionName.asftcf},
        RegionName.bbpl: {name for name, data in all_location_table.items()
                          if data.region == RegionName.bbpl or data.region == RegionName.bbplf},
        RegionName.tjm: {name for name, data in all_location_table.items()
                         if data.region == RegionName.tjm or data.region == RegionName.tjmf},
        RegionName.tlotn: {name for name, data in all_location_table.items()
                           if data.region == RegionName.tlotn or data.region == RegionName.tlotnf},
        RegionName.dol: {name for name, data in all_location_table.items()
                         if data.region == RegionName.dol or data.region == RegionName.dolf},
        RegionName.sh: {name for name, data in all_location_table.items() if data.region == RegionName.sh},
        RegionName.bc: {name for name, data in all_location_table.items() if data.region == RegionName.bc},
        RegionName.aa: {name for name, data in all_location_table.items() if data.region == RegionName.aa},
    }

    def generate_early(self):
        self.validate_yaml()
        self.multiworld.push_precollected(self.create_item(ItemName.ycbob_lvl))
        self.multiworld.push_precollected(self.create_item(ItemName.trmaw_lvl))
        self.multiworld.push_precollected(self.create_item(ItemName.batman_unlocked))
        self.multiworld.push_precollected(self.create_item(ItemName.robin_unlocked))

    def validate_yaml(self):
        if self.options.EndGoal.value == 0 and self.options.minikit_sanity.value == 0:
            raise OptionError("Minikit Win Con Requires Minikit Sanity to be enabled.")
        if self.options.high_multiplier_minimum.value < self.options.low_multiplier_minimum.value:
            raise OptionError("High Multiplier Minimum must be greater than Low Multiplier Minimum.")

    def create_regions(self):
        self.seed_location_table = setup_locations(self.options)
        create_regions(self.multiworld, self.player, self.seed_location_table)
        create_events(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = LB1Item(name, data.classification, data.code, self.player)
        return item

    def create_items(self):
        self.seed_item_table = setup_items(self.options)
        self.multiworld.itempool += [self.create_item(item_name) for item_name in self.seed_item_table]

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)
        set_event_rules(self.multiworld, self.player)

    def collect(self, state: CollectionState, item: Item) -> bool:
        changed = super().collect(state, item)
        if changed:
            name = item.name
            if name in minikit_names_set and state.count(name, self.player) == 1 and self.options.EndGoal.value == 0:
                # Count was 0 before super().collect().
                # Increase unique minikit count.
                state.prog_items[self.player]["UNIQUE_MINIKITS"] += 1
        return changed

    def remove(self, state: CollectionState, item: Item) -> bool:
        changed = super().remove(state, item)
        if changed:
            name = item.name
            if name in minikit_names_set and state.count(name, self.player) == 0 and self.options.EndGoal.value == 0:
                # Count was 1 before super().remove().
                # Decrease unique minikit count.
                state.prog_items[self.player]["UNIQUE_MINIKITS"] -= 1
        return changed

    def fill_slot_data(self):
        return {
            "EndGoal": self.options.EndGoal.value,
            "MinikitSanity": self.options.minikit_sanity.value,
            "MinikitsToWin": self.options.minikits_to_win.value,
            "LevelsToWin": self.options.levels_to_win.value,
            "TrueStatusSanity": self.options.true_status_sanity.value,
            "FreeplayOrStory": self.options.freeplay_or_story.value,
            "DecoupledTokens": self.options.decouple_character_tokens.value,
        }
