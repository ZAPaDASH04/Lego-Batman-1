from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, PerGameCommonOptions

class Goal(Choice):
    """
    Determine the goal for the seed

    Minikits: Collect all the Minikits and beat the two bonus levels to win.
    """
    display_name = "Goal"
    option_kits = 0
    default = 0


class MiniKitSanity(DefaultOnToggle):
    """
    Puts all 300 Minikits into the pool. This setting is forced on Minikit Goal
    """
    display_name = "MinikitSanity"


# class HostageSanity(Toggle):
#     """
#     Puts all 25 Hostages into the pool.
#     """
#     display_name = "HostageSanity"

#TODO: look into what option groups are

@dataclass
class LB1Options(PerGameCommonOptions):
    goal: Goal
    kit_sanity: MiniKitSanity