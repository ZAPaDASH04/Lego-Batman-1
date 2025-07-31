from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, PerGameCommonOptions

class Goal(Choice):
    """
    Determine the goal for the seed

    Hero Levels: Unlock and complete all hero campaigns levels to win.

    Villain Levels: Unlock and complete all villain campaigns levels to win.

    All Levels: Unlock and complete both campaigns to win.

    Minikits: Collect all the Minikits and beat the two bonus levels to win.

    Unlock Hush: Collect all Hostages and buy Hush

    Unlock Ra Sha Guul: Also known as 100%, Almost every single item is needed
    """
    display_name = "Goal"
    option_hero_levels = 0
    option_villain_levels = 1
    option_all_levels = 2
    option_kits = 3
    option_hush = 4
    option_ra_sha_guul = 5
    default = 0


class MiniKitSanity(Toggle):
    """
    Puts all 300 Minikits into the pool. This setting is forced on Minikit Goal
    """
    display_name = "MinikitSanity"


class HostageSanity(Toggle):
    """
    Puts all 25 Hostages into the pool.
    """
    display_name = "HostageSanity"
