from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Choice, PerGameCommonOptions, OptionList


class EndGoal(Choice):
    """
    Determine the goal for the seed

    Minikits: Collect Minikits to win.
    Levels Beaten: Beat Levels to win.
    """
    display_name = "Goal"
    option_minikits = 0
    option_levels_beaten = 1
    default = 0


class MiniKitSanity(DefaultOnToggle):
    """
    Puts all 300 Minikits into the pool.
    """
    display_name = "Minikit Sanity"


class MinikitsToWin(Range):
    """
    Number of Minikits needed to win. Only applicable if win con is set to Minikits Collected.
    """
    display_name = "Total Minikits"
    range_start = 50
    range_end = 300
    default = 200


class LevelsToWin(Range):
    """
    Number of Levels Beaten needed to win. Only applicable if win con is set to Levels Beaten.
    """
    display_name = "Total Levels"
    range_start = 5
    range_end = 30
    default = 20


class TrueStatusSanity(DefaultOnToggle):
    """
    Shuffles the true status of each level.
    """
    display_name = "True Status Sanity"


class DecoupleCharacterTokens(DefaultOnToggle):
    """
    This setting adds character tokens into the multiworld. Character tokens are required for any character purchase.
    """
    display_name = "Decouple Character Tokens"


# class HostageSanity(Toggle):
#     """
#     Puts all 25 Hostages into the pool.
#     """
#     display_name = "HostageSanity"

class FreeplayOrStoryUnlocked(DefaultOnToggle):
    """
    Determines if the level unlocked item gives you Story Mode or Story Mode & Freeplay.
    If turned off, Freeplay is unlocked by completing Story Mode.
    """
    display_name = "Unlock Story or Story and Freeplay"


class StartingHeroLevelCount(Range):
    """
    Determine the number of hero levels you start with.
    """
    display_name = "Starting Hero Level Count"
    range_start = 1
    range_end = 15
    default = 1


class StartingHeroLevelOptions(OptionList):
    """
    Determines which hero levels you can start with.

    Valid Keys:
    "You can Bank on Batman"
    "An Icy Reception"
    "Two-Face Chase"
    "A Poisonous Appointment"
    "The Face-Off"
    "There She Goes Again"
    "Batboat Battle"
    "Under the City"
    "Zoo's Company"
    "Penguin's Lair"
    "Joker's Home Turf"
    "Little Fun at the Big Top"
    "Flight of the Bat"
    "In the Dark Night"
    "To the Top of the Tower"
    """

    display_name = "Starting Hero Level Options"

    valid_keys = {
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
    }

    default = [
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


class StartingVillainLevelCount(Range):
    """
    Determine the number of villain levels you start with.
    """
    display_name = "Starting Villain Level Count"
    range_start = 1
    range_end = 15
    default = 1


class StartingVillainLevelOptions(OptionList):
    """
    Determines which villain levels you can start with.

    Valid Keys:
    "The Riddler Makes a Withdrawal"
    "On the Rocks"
    "Green Fingers"
    "An Enterprising Theft"
    "Breaking Blocks"
    "Rockin' the Docks"
    "Stealing the Show"
    "Harbouring a Grudge"
    "A Daring Rescue"
    "Arctic World"
    "A Surprise for the Commissioner"
    "Biplane Blast"
    "The Joker's Masterpiece"
    "The Lure of the Night"
    "Dying of Laughter"
    """

    display_name = "Starting Villain Level Options"

    valid_keys = {
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
    }

    default = [
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


class ShopPurchasesRequireMultiplier(DefaultOnToggle):
    """
    Determines if shop purchases require a score multiplier.
    """
    display_name = "Shop Purchases Require Multiplier"


class LowMultiplierPriceMinimum(Range):
    """
    Determines the starting price for a low multiplier. Does nothing if Shop Purchases Require Multiplier is disabled.
    A low multiplier is defined as any multiplier.
    """
    display_name = "Low Multiplier Price Minimum"
    range_start = 10
    range_end = 10000000
    default = 50000


class HighMultiplierMinimum(Range):
    """
    Determines the starting price for a high multiplier. Does nothing if Shop Purchases Require Multiplier is disabled.
    Must be larger than Low Multiplier Price.
    A high multiplier is defined as Score x6, Score x8, Score x10 or both Score x2 and Score x4.
    """
    display_name = "High Multiplier Price Minimum"
    range_start = 10
    range_end = 10000000
    default = 100000


class ShuffleHushAndRas(DefaultOnToggle):
    """
    Determines if the purchases for Hush and Ras are shuffled in the Item Pool.
    """
    display_name = "Shuffle Hush and Ra's al Ghul"


class DecoupleShuffleHushAndRasToken(DefaultOnToggle):
    """
    Determines if the Character Token for Hush and Ras are shuffled in the Item Pool.
    """
    display_name = "Decouple Hush and Ra's al Ghul's Character Token"


class HushPurchaseRequirements(Range):
    """
    Determine the number of Hostages needed to unlock the Hush Purchase.
    """
    display_name = "Hush Purchase Requirements"
    range_start = 0
    range_end = 25
    default = 12


class RasPurchaseRequirements(Range):
    """
    Determine the number of Minikits needed to unlock the Ra's al Ghul Purchase.
    """
    display_name = "Ra's al Ghul Purchase Requirements"
    range_start = 0
    range_end = 300
    default = 150


# TODO: look into what option groups are
@dataclass
class LB1Options(PerGameCommonOptions):
    EndGoal: EndGoal
    minikit_sanity: MiniKitSanity
    minikits_to_win: MinikitsToWin
    levels_to_win: LevelsToWin
    true_status_sanity: TrueStatusSanity
    freeplay_or_story: FreeplayOrStoryUnlocked
    starting_hero_level_count: StartingHeroLevelCount
    starting_hero_level_options: StartingHeroLevelOptions
    starting_villain_level_count: StartingVillainLevelCount
    starting_villain_level_options: StartingVillainLevelOptions
    shop_purchases_required_multiplier: ShopPurchasesRequireMultiplier
    low_multiplier_minimum: LowMultiplierPriceMinimum
    high_multiplier_minimum: HighMultiplierMinimum
    decouple_character_tokens: DecoupleCharacterTokens
    shuffle_hush_and_ras: ShuffleHushAndRas
    decouple_hush_and_ras_token: DecoupleShuffleHushAndRasToken
    hush_purchase_requirements: HushPurchaseRequirements
    ras_purchase_requirements: RasPurchaseRequirements
    # hostage_sanity: HostageSanity
