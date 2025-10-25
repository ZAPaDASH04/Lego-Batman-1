from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Choice, PerGameCommonOptions


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


# TODO: look into what option groups are
@dataclass
class LB1Options(PerGameCommonOptions):
    EndGoal: EndGoal
    minikit_sanity: MiniKitSanity
    minikits_to_win: MinikitsToWin
    levels_to_win: LevelsToWin
    true_status_sanity: TrueStatusSanity
    decouple_character_tokens: DecoupleCharacterTokens
    freeplay_or_story: FreeplayOrStoryUnlocked
    shop_purchases_required_multiplier: ShopPurchasesRequireMultiplier
    low_multiplier_minimum: LowMultiplierPriceMinimum
    high_multiplier_minimum: HighMultiplierMinimum
    # hostage_sanity: HostageSanity
