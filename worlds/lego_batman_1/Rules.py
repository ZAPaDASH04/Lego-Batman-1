from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import CollectionState

from .Locations import level_beaten_event_location_table
from .Names import LocationName, ItemName, RegionName
from .Options import LB1Options, EndGoal


def char_can_cross_toxic(state: CollectionState, player: int):
    return (
            state.has(ItemName.mrfreeze_unlocked, player)
            or state.has(ItemName.poisonivy_unlocked, player)
            or state.has(ItemName.twoface_unlocked, player)
            or state.has(ItemName.bane_unlocked, player)
            or state.has(ItemName.killercroc_unlocked, player)
            or state.has(ItemName.joker_unlocked, player)
            or state.has(ItemName.jokertropical_unlocked, player)
    )


def char_can_double_jump(state: CollectionState, player: int):
    return (
            state.has(ItemName.clayface_unlocked, player)
            or state.has(ItemName.poisonivy_unlocked, player)
            or state.has(ItemName.catwoman_unlocked, player)
            or state.has(ItemName.catwomanclassic_unlocked, player)
            or state.has(ItemName.harleyquinn_unlocked, player)
            or state.has(ItemName.madhatter_unlocked, player)
    )


def char_can_access_female_room(state: CollectionState, player: int):
    return (
            state.has(ItemName.poisonivy_unlocked, player)
            or state.has(ItemName.harleyquinn_unlocked, player)
            or state.has(ItemName.catwoman_unlocked, player)
            or state.has(ItemName.catwomanclassic_unlocked, player)
    )


def char_can_hypno(state: CollectionState, player: int):
    return (
            state.has(ItemName.riddler_unlocked, player)
            or state.has(ItemName.scarecrow_unlocked, player)
            or state.has(ItemName.madhatter_unlocked, player)
    )


def char_joker(state: CollectionState, player: int):
    return (
            state.has(ItemName.joker_unlocked, player)
            or state.has(ItemName.jokertropical_unlocked, player)
    )


def char_is_strong(state: CollectionState, player: int):
    return (
            state.has(ItemName.clayface_unlocked, player)
            or state.has(ItemName.mrfreeze_unlocked, player)
            or state.has(ItemName.bane_unlocked, player)
            or state.has(ItemName.killercroc_unlocked, player)
            or state.has(ItemName.manbat_unlocked, player)
    )


def char_can_glide(state: CollectionState, player: int):
    return (
            state.has(ItemName.glidesuit, player)
            or state.has(ItemName.manbat_unlocked, player)
            or state.has(ItemName.penguin_unlocked, player)
            or state.has(ItemName.killermoth_unlocked, player)
    )


def char_can_long_jump(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            or char_can_glide(state, player)
    )


def char_can_sink(state: CollectionState, player: int):
    return (
            state.has(ItemName.watersuit, player)
            or state.has(ItemName.killercroc_unlocked, player)
    )


def char_can_explode(state: CollectionState, player: int):
    return (
            state.has(ItemName.demolitionsuit, player)
            or state.has(ItemName.penguin_unlocked, player)
    )


def char_can_techno(state: CollectionState, player: int):
    return (
            state.has(ItemName.techsuit, player)
            or state.has(ItemName.scientist_unlocked, player)
    )


def auto_has_cable(state: CollectionState, player: int):
    return (
            state.has(ItemName.batmobile_unlocked, player)
            or state.has(ItemName.batcycle_unlocked, player)
            or state.has(ItemName.battank_unlocked, player)
            or state.has(ItemName.catmotorcycle_unlocked, player)
    )


def auto_can_explode(state: CollectionState, player: int):
    return (
            state.has(ItemName.policecar_unlocked, player)
            or state.has(ItemName.policevan_unlocked, player)
            or state.has(ItemName.hammertruck_unlocked, player)
            or state.has(ItemName.jokervan_unlocked, player)
            or state.has(ItemName.garbagetruck_unlocked, player)
    )


def water_has_torpedo(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinswatercraft_unlocked, player)
            or state.has(ItemName.penguinsubmarine_unlocked, player)
    )


def water_can_sink(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinssubmarine_unlocked, player)
            or state.has(ItemName.penguinsubmarine_unlocked, player)
            or state.has(ItemName.penguingoonsub_unlocked, player)
    )


def water_can_cross_toxic(state: CollectionState, player: int):
    return (
            state.has(ItemName.policewatercraft_unlocked, player)
            or state.has(ItemName.swamprider_unlocked, player)
            or state.has(ItemName.iceberg_unlocked, player)
    )


def air_has_cable(state: CollectionState, player: int):
    return (
            state.has(ItemName.batcopter_unlocked, player)
            or state.has(ItemName.harbourhelicopter_unlocked, player)
            or state.has(ItemName.policehelicopter_unlocked, player)
            or state.has(ItemName.jokerhelicopter_unlocked, player)
            or state.has(ItemName.goonhelicopter_unlocked, player)
    )


def air_can_cross_toxic(state: CollectionState, player: int):
    return (
            state.has(ItemName.harbourhelicopter_unlocked, player)
            or state.has(ItemName.policehelicopter_unlocked, player)
            or state.has(ItemName.jokerhelicopter_unlocked, player)
            or state.has(ItemName.scarecrowbiplane_unlocked, player)
            or state.has(ItemName.goonhelicopter_unlocked, player)
    )


def can_beat_ycbob(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_air(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_glide(state, player)
        )


def can_beat_apa(state: CollectionState, player: int):
    return (
            state.has(ItemName.attractsuit, player)
            and state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_beat_tfo(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and (state.has(ItemName.attractsuit, player) or char_can_cross_toxic(state, player))
        )


def can_beat_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_utc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.watersuit, player)
                and state.has(ItemName.demolitionsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_sink(state, player)
                and char_can_explode(state, player)
        )


def can_beat_zc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.techsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_beat_pl(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.watersuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_sink(state, player)
        )


def can_beat_jht(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_beat_lfabt(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.sonicsuit, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_beat_itdn(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_tttot(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_glide(state, player)
        )


# Whole level locked by glide
def level_access_tfo(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.tfo_lvl, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.tfo_lvl, player)
        )


# Whole level locked by Attract Suit & Glide
def level_access_jht(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.attractsuit, player)
                and state.has(ItemName.jht_lvl, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.attractsuit, player)
                and state.has(ItemName.jht_lvl, player)
        )


# Free Access functions are needed for moving about in freeplay (moves story characters have)
def free_access_ycbob(state: CollectionState, player: int):
    return char_can_explode(state, player)


def free_access_air(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and char_can_glide(state, player)
    )


def free_access_tfc(state: CollectionState, player: int):
    return auto_has_cable(state, player)


def free_access_apa(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.attractsuit, player)
    )


def free_access_tfo(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def free_access_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.magsuit, player)
        )


def free_access_bbb(state: CollectionState, player: int):
    return state.has(ItemName.batboat_unlocked, player)


def free_access_utc(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_sink(state, player)
            and (state.has(ItemName.magsuit, player) or char_can_glide(state, player))
    )


def free_access_zc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.glidesuit, player)
        )
    return (
            char_can_explode(state, player)
            or (state.has(ItemName.magsuit, player) and char_can_glide(state, player))
    )


def free_access_pl(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.glidesuit, player)
                and state.has(ItemName.watersuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_sink(state, player)
        )


def free_access_lfabt(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.demolitionsuit, player)
    else:
        return char_can_explode(state, player)


def free_access_itdn(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.demolitionsuit, player)
    else:
        return char_can_explode(state, player)


def free_access_tttot(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def free_access_trmaw(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
    )


def free_access_otr(state: CollectionState, player: int):
    return state.has(ItemName.mrfreeze_unlocked, player)


def free_access_gf(state: CollectionState, player: int):
    return char_can_hypno(state, player)


def free_access_bb(state: CollectionState, player: int):
    return char_can_hypno(state, player)


def free_access_rtd(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
    )


def free_access_sts(state: CollectionState, player: int):
    return (
            char_can_glide(state, player)
            and char_can_access_female_room(state, player)
    )


def free_access_hag(state: CollectionState, player: int):
    return water_has_torpedo(state, player)


def free_access_adr(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and char_can_cross_toxic(state, player)
            and (char_can_double_jump(state, player) or char_can_glide(state, player))
    )


def free_access_aw(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def free_access_asftc(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def free_access_bbpl(state: CollectionState, player: int):
    return (
            air_has_cable(state, player)
            and state.has(ItemName.batwing_unlocked, player)
    )


def free_access_tjm(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_hypno(state, player)
    )


def free_access_tlotn(state: CollectionState, player: int):
    return char_joker(state, player)


def free_access_dol(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_double_jump(state, player)
    )


def can_ycbob_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return state.has(ItemName.sonicsuit, player)


def can_ycbob_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and char_can_cross_toxic(state, player)
                and char_is_strong(state, player)
                and char_can_hypno(state, player)
        )
    else:
        return (
                char_can_cross_toxic(state, player)
                and char_is_strong(state, player)
                and char_can_hypno(state, player)
        )


def can_ycbob_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_ycbob_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_ycbob_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_ycbob_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and state.has(ItemName.attractsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                state.has(ItemName.attractsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_ycbob_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_ycbob(state, options, player)
                and char_can_hypno(state, player)
                and char_can_techno(state, player)
        )
    else:
        return (
                char_can_hypno(state, player)
                and char_can_techno(state, player)
        )


def can_ycbob_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.attractsuit, player)
    else:
        return char_can_techno(state, player)


def can_air_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_double_jump(state, player)
        )
    else:
        return char_can_double_jump(state, player)


def can_air_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_double_jump(state, player)
        )
    else:
        return char_can_double_jump(state, player)


def can_air_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_air_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_double_jump(state, player)
                and char_can_hypno(state, player)
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_hypno(state, player)
        )


def can_air_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_double_jump(state, player)
                and char_can_explode(state, player)
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_explode(state, player)
        )


def can_air_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_access_female_room(state, player)
        )
    else:
        return char_can_access_female_room(state, player)


def can_air_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_cross_toxic(state, player)
                and char_can_explode(state, player)
        )
    else:
        return (
                char_can_cross_toxic(state, player)
                and char_can_explode(state, player)
        )


def can_air_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_explode(state, player)
        )
    else:
        return char_can_explode(state, player)


def can_air_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_hypno(state, player)
        )
    else:
        return char_can_hypno(state, player)


def can_tfc_min7(state: CollectionState, player: int):
    return state.has(ItemName.jokervan_unlocked, player)


def can_tfc_min8(state: CollectionState, player: int):
    return state.has(ItemName.hammertruck_unlocked, player)


def can_tfc_min10(state: CollectionState, player: int):
    return auto_can_explode(state, player)


def can_apa_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and char_can_double_jump(state, player)
                and char_can_glide(state, player)
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_glide(state, player)
        )


def can_apa_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and char_can_techno(state, player)
        )
    else:
        return (
                state.has(ItemName.sonicsuit, player)
                and state.has(ItemName.heatprotectsuit, player)
                and char_can_techno(state, player)
        )


def can_apa_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )


def can_apa_min5(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_apa_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and char_can_sink(state, player)
        )
    else:
        return char_can_sink(state, player)


def can_apa_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_explode(state, player)
        )


def can_apa_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and state.has(ItemName.heatprotectsuit, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                state.has(ItemName.heatprotectsuit, player)
                and char_can_double_jump(state, player)
        )


def can_apa_min9(state: CollectionState, player: int):
    return state.has(ItemName.heatprotectsuit, player)


def can_apa_min10(state: CollectionState, player: int):
    return state.has(ItemName.heatprotectsuit, player)


def can_tfo_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_techno(state, player)
        )
    else:
        return char_can_techno(state, player)


def can_tfo_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_double_jump(state, player)
                # Attract suit part of can beat level
        )
    else:
        return (
                char_can_double_jump(state, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_tfo_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return char_can_cross_toxic(state, player)


def can_tfo_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return char_can_cross_toxic(state, player)


def can_tfo_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and state.has(ItemName.mrfreeze_unlocked, player)
                and state.has(ItemName.poisonivy_unlocked, player)
        )
    else:
        return (
                state.has(ItemName.mrfreeze_unlocked, player)
                and state.has(ItemName.poisonivy_unlocked, player)
        )


def can_tfo_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.attractsuit, player)
    else:
        return state.has(ItemName.attractsuit, player) or char_can_cross_toxic(state, player)


def can_tfo_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.attractsuit, player)
    else:
        return state.has(ItemName.attractsuit, player) or char_can_cross_toxic(state, player)


def can_tsga_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and state.has(ItemName.magsuit, player)
                and char_can_access_female_room(state, player)
        )
    else:
        return (
                state.has(ItemName.magsuit, player)
                and char_can_access_female_room(state, player)
        )


def can_tsga_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )


def can_tsga_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_can_sink(state, player)
                # Explosives checked for as part of can beat tsga
            )
    else:
        return (
                char_can_sink(state, player)
                and char_can_explode(state, player)
        )


def can_tsga_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
                # Explosives checked for as part of can beat tsga
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_explode(state, player)
        )


def can_tsga_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_can_sink(state, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return (
                char_can_sink(state, player)
                and char_can_cross_toxic(state, player)
        )


def can_tsga_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_tsga_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
                # Explosives checked for as part of can beat tsga
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
                and char_can_explode(state, player)
        )


def can_tsga_min9(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and state.has(ItemName.sonicsuit, player)
            # Explosives checked for as part of can beat tsga
            # Techno checked for as part of can beat tsga
    )


def can_tsga_min10(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
            # Explosives checked for as part of can beat tsga
            # Techno checked for as part of can beat tsga
    )


def can_bbb_min3(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinswatercraft_unlocked, player)
            and water_can_sink(state, player)
    )


def can_bbb_min5(state: CollectionState, player: int):
    return water_can_sink(state, player)


def can_bbb_min6(state: CollectionState, player: int):
    return water_can_cross_toxic(state, player)


def can_bbb_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinswatercraft_unlocked, player)
            and state.has(ItemName.penguinsubmarine_unlocked, player)
    )


def can_bbb_min10(state: CollectionState, player: int):
    return (
            state.has(ItemName.robinswatercraft_unlocked, player)
            and state.has(ItemName.penguinsubmarine_unlocked, player)
            and water_can_cross_toxic(state, player)
    )


def can_utc_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_can_double_jump(state, player)
                # Explosives checked for as part of level clear
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_explode(state, player)
        )


def can_utc_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_can_hypno(state, player)
                and (state.has(ItemName.mrfreeze_unlocked, player) or state.has(ItemName.bane_unlocked, player)
                     or state.has(ItemName.killercroc_unlocked, player))
                # Explosives and glide checked for as part of level clear
        )
    else:
        return (
                char_can_hypno(state, player)
                and char_can_explode(state, player)
                and char_can_glide(state, player)
                and (state.has(ItemName.mrfreeze_unlocked, player) or state.has(ItemName.bane_unlocked, player)
                     or state.has(ItemName.killercroc_unlocked, player))
        )


def can_utc_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and state.has(ItemName.sonicsuit, player)
                and char_is_strong(state, player)
                # Explosives and sink checked for as part of level clear
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_sink(state, player)
                and char_is_strong(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_utc_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_can_double_jump(state, player)
                # Explosives and sink checked for as part of level clear
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_explode(state, player)
                and char_can_sink(state, player)
        )


def can_utc_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return state.has(ItemName.attractsuit, player)


def can_utc_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return char_can_cross_toxic(state, player)


def can_utc_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_utc_min8(state: CollectionState, options: LB1Options, player: int):
    # Obtainable with Region Access
    if options.freeplay_or_story == 0:
        return can_beat_utc(state, options, player)
    else:
        return True


def can_utc_min9(state: CollectionState, options: LB1Options, player: int):
    # Obtainable with Region Access
    if options.freeplay_or_story == 0:
        return can_beat_utc(state, options, player)
    else:
        return True


def can_utc_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_joker(state, player)
        )
    else:
        return char_joker(state, player)


def can_zc_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_can_access_female_room(state, player)
                # Explosives part of can beat level
        )
    else:
        return (
                char_can_access_female_room(state, player)
                and char_can_explode(state, player)
        )


def can_zc_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
                and char_can_cross_toxic(state, player)
        )


def can_zc_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return state.has(ItemName.attractsuit, player)


def can_zc_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_can_double_jump(state, player)
                # Explosive checked for as part of beat level
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_explode(state, player)
        )


def can_zc_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and state.has(ItemName.poisonivy_unlocked, player)
        )
    else:
        return state.has(ItemName.poisonivy_unlocked, player)


def can_zc_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return True
    else:
        return char_can_long_jump(state, player)


def can_zc_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.techsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_zc_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and state.has(ItemName.mrfreeze_unlocked, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.sonicsuit, player)
                and state.has(ItemName.mrfreeze_unlocked, player)
        )


def can_zc_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and state.has(ItemName.sonicsuit, player)
                and char_is_strong(state, player)
        )


def can_pl_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return state.has(ItemName.sonicsuit, player)


def can_pl_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and state.has(ItemName.mrfreeze_unlocked, player)
                and char_can_explode(state, player)
        )
    else:
        return (
                state.has(ItemName.mrfreeze_unlocked, player)
                and char_can_explode(state, player)
        )


def can_pl_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_double_jump(state, player)
        )


# with region access, can beat level in story
def can_pl_min7(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_pl_min8(state: CollectionState, player: int):
    return (
            char_can_cross_toxic(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_pl_min10(state: CollectionState, player: int):
    return (
            state.has(ItemName.heatprotectsuit, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_jht_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_explode(state, player)
        )
    else:
        return char_can_explode(state, player)


def can_jht_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_hypno(state, player)
                and char_can_explode(state, player)
                and state.has(ItemName.heatprotectsuit, player)
        )
    else:
        return (
                char_can_hypno(state, player)
                and char_can_explode(state, player)
                and state.has(ItemName.heatprotectsuit, player)
        )


def can_jht_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_joker(state, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_joker(state, player)
                and char_can_double_jump(state, player)
        )


def can_jht_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_techno(state, player)
        )
    else:
        return char_can_techno(state, player)


def can_jht_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return char_can_cross_toxic(state, player)


def can_jht_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )


def can_jht_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return char_can_cross_toxic(state, player)


def can_jht_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_joker(state, player)
                # Mag suit checked for as part of beat story
        )
    else:
        return (
                char_joker(state, player)
                and state.has(ItemName.magsuit, player)
        )


def can_jht_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_explode(state, player)
                # Mag suit checked for as part of beat story
        )
    else:
        return (
                char_can_explode(state, player)
                and state.has(ItemName.magsuit, player)
        )


def can_lfabt_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_double_jump(state, player)
        )


def can_lfabt_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_can_long_jump(state, player)
                # Sonic Suit checked as part of can beat
        )
    else:
        return (
                char_can_long_jump(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_lfabt_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_can_sink(state, player)
        )
    else:
        return char_can_sink(state, player)


def can_lfabt_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_can_techno(state, player)
        )
    else:
        return char_can_techno(state, player)


def can_lfabt_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.sonicsuit, player)
    else:
        return (
                char_can_explode(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_lfabt_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_joker(state, player)
        )
    else:
        return (
                char_joker(state, player)
                and state.has(ItemName.sonicsuit, player)
                and state.has(ItemName.magsuit, player)
        )


def can_lfabt_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return can_beat_lfabt(state, options, player)
    else:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.attractsuit, player)
        )


def can_lfabt_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_can_techno(state, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return (
                state.has(ItemName.attractsuit, player)
                and state.has(ItemName.magsuit, player)
                and char_can_techno(state, player)
                and char_can_cross_toxic(state, player)
        )


def can_lfabt_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return (
                state.has(ItemName.attractsuit, player)
                and state.has(ItemName.magsuit, player)
                and char_is_strong(state, player)
        )


def can_lfabt_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return (
                state.has(ItemName.attractsuit, player)
                and state.has(ItemName.magsuit, player)
                and char_can_cross_toxic(state, player)
        )


def can_fotb_min7(state: CollectionState, player: int):
    return (
            air_can_cross_toxic(state, player)
            and state.has(ItemName.batwing_unlocked, player)
            and air_has_cable(state, player)
    )


def can_fotb_min9(state: CollectionState, player: int):
    return (
            air_can_cross_toxic(state, player)
            and state.has(ItemName.batwing_unlocked, player)
            and air_has_cable(state, player)
    )


def can_itdn_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_is_strong(state, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_itdn_min2(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_can_long_jump(state, player)
        )
    else:
        return char_can_long_jump(state, player)


def can_itdn_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_can_hypno(state, player)
                and char_is_strong(state, player)
                and char_can_cross_toxic(state, player)
                and char_can_double_jump(state, player)
                and state.has(ItemName.penguin_unlocked, player)
        )
    else:
        return (
                char_can_hypno(state, player)
                and char_is_strong(state, player)
                and char_can_cross_toxic(state, player)
                and char_can_double_jump(state, player)
                and state.has(ItemName.penguin_unlocked, player)
        )


def can_itdn_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_can_sink(state, player)
                and state.has(ItemName.poisonivy_unlocked, player)
        )
    else:
        return (
                char_can_sink(state, player)
                and state.has(ItemName.poisonivy_unlocked, player)
        )


def can_itdn_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_can_techno(state, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return (
                state.has(ItemName.attractsuit, player)
                and char_can_techno(state, player)
        )


def can_itdn_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_can_techno(state, player)
                and char_is_strong(state, player)
        )
    else:
        return (
                char_is_strong(state, player)
                and char_can_techno(state, player)
        )


def can_itdn_min7(state: CollectionState, options: LB1Options, player: int):
    return can_beat_itdn(state, options, player)


def can_itdn_min8(state: CollectionState, options: LB1Options, player: int):
    return can_beat_itdn(state, options, player)


def can_itdn_min9(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_itdn(state, options, player)
            and char_joker(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_itdn_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_joker(state, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return (
                char_joker(state, player)
                and state.has(ItemName.sonicsuit, player)
        )


def can_tttot_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and char_can_explode(state, player)
        )
    else:
        return char_can_explode(state, player)


def can_tttot_min3(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return state.has(ItemName.sonicsuit, player)


def can_tttot_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and state.has(ItemName.attractsuit, player)
        )
    else:
        return state.has(ItemName.attractsuit, player)


def can_tttot_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and char_can_long_jump(state, player)
        )
    else:
        return char_can_long_jump(state, player)


def can_tttot_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and char_joker(state, player)
        )
    else:
        return char_joker(state, player)


def can_tttot_min9(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_double_jump(state, player)
        )


def can_tttot_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return can_beat_tttot(state, options, player)
    else:
        return (
                can_beat_tttot(state, options, player)
                and char_can_explode(state, player)
        )


def can_trmaw_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_trmaw_min6_and_9(state: CollectionState, player: int):
    return (
            (char_can_explode(state, player) and state.has(ItemName.sonicsuit, player))
            or (char_can_double_jump(state, player) and state.has(ItemName.sonicsuit, player))
    )


def can_otr_min2(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and char_can_hypno(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_otr_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_otr_min5(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def can_otr_min7(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and state.has(ItemName.attractsuit, player)
    )


def can_otr_min8(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and char_can_explode(state, player)
    )


def can_otr_min9(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and state.has(ItemName.magsuit, player)
            and char_can_glide(state, player)
    )


def can_gf_min1(state: CollectionState, player: int):
    return char_can_techno(state, player)


def can_gf_min2(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_double_jump(state, player)
    )


def can_gf_min4(state: CollectionState, player: int):
    return (
            char_can_cross_toxic(state, player)
            and char_can_explode(state, player)
    )


def can_gf_min5(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_gf_min6(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_gf_min7(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
            and state.has(ItemName.magsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_gf_min8(state: CollectionState, player: int):
    return (
            char_can_cross_toxic(state, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_gf_min9(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_gf_min10(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_min1(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_aet_min2(state: CollectionState, player: int):
    return (
            char_can_techno(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_aet_min3(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_aet_min4(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_aet_min5(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_techno(state, player)
    )


def can_aet_min7(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_aet_min8(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_aet_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.heatprotectsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_min2(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_bb_min4(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.attractsuit, player)
            and state.has(ItemName.magsuit, player)
    )


def can_bb_min5(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_bb_min6(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_bb_min7(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and char_joker(state, player)
    )


def can_bb_min8(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.magsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_min10(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_rtd_min1(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_can_double_jump(state, player)
    )


def can_rtd_min2(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_rtd_min5(state: CollectionState, player: int):
    return state.has(ItemName.poisonivy_unlocked, player)


def can_rtd_min7(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_techno(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_rtd_min9(state: CollectionState, player: int):
    return (
            char_can_access_female_room(state, player)
            and state.has(ItemName.attractsuit, player)
            and char_can_cross_toxic(state, player)
    )


def can_sts_min1(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and state.has(ItemName.magsuit, player)
    )


def can_sts_min3(state: CollectionState, player: int):
    return (
            char_can_glide(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_sts_min6(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def can_sts_min7(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_is_strong(state, player)
    )


def can_sts_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_sts_min10(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_hag_min3(state: CollectionState, player: int):
    return state.has(ItemName.batboat_unlocked, player)


def can_hag_min8(state: CollectionState, player: int):
    return state.has(ItemName.batboat_unlocked, player)


def can_hag_min10(state: CollectionState, player: int):
    return state.has(ItemName.robinswatercraft_unlocked, player)


def can_adr_min2(state: CollectionState, player: int):
    return char_joker(state, player)


def can_adr_min3(state: CollectionState, player: int):
    return state.has(ItemName.heatprotectsuit, player)


def can_adr_min5(state: CollectionState, player: int):
    return (
            state.has(ItemName.attractsuit, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_adr_min6(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and state.has(ItemName.mrfreeze_unlocked, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_adr_min7(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_adr_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_aw_min1(state: CollectionState, player: int):
    return char_can_sink(state, player)


def can_aw_min2(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and state.has(ItemName.magsuit, player)
            and char_joker(state, player)
            and char_is_strong(state, player)
            and char_can_double_jump(state, player)
    )


def can_aw_min3(state: CollectionState, player: int):
    return (
            state.has(ItemName.sonicsuit, player)
            and char_can_double_jump(state, player)
    )


def can_aw_min4(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and char_can_access_female_room(state, player)
            and char_can_double_jump(state, player)
            and char_can_explode(state, player)
    )


def can_aw_min5(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_aw_min6(state: CollectionState, player: int):
    return (
        char_is_strong(state, player)
        and char_can_cross_toxic(state, player)
    )


def can_aw_min8(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_access_female_room(state, player)
    )


def can_aw_min9(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and char_can_access_female_room(state, player)
    )


def can_aw_min10(state: CollectionState, player: int):
    return (
            state.has(ItemName.mrfreeze_unlocked, player)
            and char_can_access_female_room(state, player)
    )


def can_asftc_min1(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_asftc_min2(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_asftc_min3(state: CollectionState, player: int):
    return (
            state.has(ItemName.mrfreeze_unlocked, player)
            and char_joker(state, player)
    )


def can_asftc_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_asftc_min5(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def can_asftc_min7(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and char_can_explode(state, player)
    )


def can_asftc_min8(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and char_joker(state, player)
    )


def can_asftc_min9(state: CollectionState, player: int):
    return (
            state.has(ItemName.attractsuit, player)
            and char_joker(state, player)
            and char_can_techno(state, player)
    )


def can_tjm_min3(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_tjm_min4(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_tjm_min5(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_tjm_min6(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_tjm_min7(state: CollectionState, player: int):
    return (
            state.has(ItemName.heatprotectsuit, player)
            and char_can_explode(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_tjm_min8(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_tjm_min9(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_tlotn_min1(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and char_can_explode(state, player)
    )


def can_tlotn_min2(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and char_can_explode(state, player)
    )


def can_tlotn_min3(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_tlotn_min4(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and (char_can_glide(state, player) or char_can_double_jump(state, player))
    )


def can_tlotn_min5(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and (char_can_glide(state, player) or char_can_double_jump(state, player))
    )


def can_tlotn_min9(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and (char_can_glide(state, player) or char_can_double_jump(state, player))
    )


def can_tlotn_min10(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and state.has(ItemName.sonicsuit, player)
            and (char_can_glide(state, player) or char_can_double_jump(state, player))
    )


def can_dol_min1(state: CollectionState, player: int):
    return state.has(ItemName.poisonivy_unlocked, player)


def can_dol_min2(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_dol_min3(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_dol_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_dol_min5(state: CollectionState, player: int):
    return state.has(ItemName.magsuit, player)


def can_dol_min7(state: CollectionState, player: int):
    return char_can_glide(state, player)


def can_dol_min8(state: CollectionState, player: int):
    return state.has(ItemName.mrfreeze_unlocked, player)


def can_dol_min10(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_air_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_can_hypno(state, player)
        )
    else:
        return char_can_hypno(state, player)


def can_apa_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_tfo_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_double_jump(state, player)
                # Attract Suit Tested as part of Level Beaten
        )
    else:
        return (
                state.has(ItemName.attractsuit, player)
                and char_can_double_jump(state, player)
        )


def can_utc_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.demolitionsuit, player)
        )
    else:
        return char_can_explode(state, player)


def can_zc_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.techsuit, player)
    else:
        return (
                state.has(ItemName.sonicsuit, player)
                or (char_can_techno(state, player) and char_can_glide(state, player))
        )


def can_jht_host(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_jht(state, options, player)
            and char_joker(state, player)
    )


def can_lfabt_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.magsuit, player)
                and state.has(ItemName.sonicsuit, player)
        )
    else:
        return state.has(ItemName.magsuit, player)


def can_itdn_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                state.has(ItemName.demolitionsuit, player)
                and state.has(ItemName.techsuit, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_trmaw_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_otr_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_gf_host(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_bb_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_rtd_host(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_sts_host(state: CollectionState, player: int):
    return (
            state.has(ItemName.magsuit, player)
            and char_is_strong(state, player)
    )


def can_adr_host(state: CollectionState, player: int):
    return char_joker(state, player)


def can_aw_host(state: CollectionState, player: int):
    return char_can_cross_toxic(state, player)


def can_asftc_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_tjm_host(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_explode(state, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_tlotn_host(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_dol_host(state: CollectionState, player: int):
    return char_can_glide(state, player)


def can_ycbob_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return state.has(ItemName.techsuit, player)
    else:
        return char_can_techno(state, player)


def can_air_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_air(state, options, player)
                and char_is_strong(state, player)
        )
    else:
        return char_is_strong(state, player)


def can_apa_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and char_can_explode(state, player)
                and char_joker(state, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_joker(state, player)
                and state.has(ItemName.heatprotectsuit, player)
        )


def can_tfo_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_cross_toxic(state, player)
        )
    else:
        return char_can_cross_toxic(state, player)


def can_tsga_rb(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and state.has(ItemName.sonicsuit, player)
            # Explosives checked for as part of can beat tsga
            # Techno checked for as part of can beat tsga
    )


def can_bbb_rb(state: CollectionState, player: int):
    return (
            state.has(ItemName.penguinsubmarine_unlocked, player)
            and state.has(ItemName.robinswatercraft_unlocked, player)
    )


def can_utc_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_can_techno(state, player)
        )
    else:
        return char_can_techno(state, player)


def can_zc_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_can_double_jump(state, player)
                and char_can_sink(state, player)
        )
    else:
        return (
                char_can_double_jump(state, player)
                and char_can_sink(state, player)
        )


def can_pl_rb(state: CollectionState, player: int):
    return state.has(ItemName.sonicsuit, player)


def can_jht_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and state.has(ItemName.mrfreeze_unlocked, player)
                and state.has(ItemName.sonicsuit, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                state.has(ItemName.mrfreeze_unlocked, player)
                and state.has(ItemName.sonicsuit, player)
                and char_can_double_jump(state, player)
        )


def can_lfabt_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_can_glide(state, player)
                and char_can_techno(state, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_techno(state, player)
        )


def can_fotb_rb(state: CollectionState, player: int):
    return (
            air_can_cross_toxic(state, player)
            and state.has(ItemName.batwing_unlocked, player)
            and air_has_cable(state, player)
    )


def can_itdn_rb(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_itdn(state, options, player)
            and char_can_glide(state, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_tttot_rb(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tttot(state, options, player)
            and char_is_strong(state, player)
    )


def can_trmaw_rb(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_otr_rb(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_gf_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.attractsuit, player)
            and char_can_techno(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_bb_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_rtd_rb(state: CollectionState, player: int):
    return (
            char_can_access_female_room(state, player)
            and char_is_strong(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_sts_rb(state: CollectionState, player: int):
    return (
            state.has(ItemName.attractsuit, player)
            and char_can_techno(state, player)
            and state.has(ItemName.penguin_unlocked, player)
            and char_can_explode(state, player)
    )


def can_hag_rb(state: CollectionState, player: int):
    return state.has(ItemName.robinswatercraft_unlocked, player)


def can_adr_rb(state: CollectionState, player: int):
    return (
            char_can_techno(state, player)
            and state.has(ItemName.penguin_unlocked, player)
            and state.has(ItemName.sonicsuit, player)
    )


def can_aw_rb(state: CollectionState, player: int):
    return char_can_cross_toxic(state, player)


def can_asftc_rb(state: CollectionState, player: int):
    return (
            char_can_glide(state, player)
            and char_can_explode(state, player)
            and char_joker(state, player)
    )


def can_tjm_rb(state: CollectionState, player: int):
    return (
            char_joker(state, player)
            and char_can_explode(state, player)
            and state.has(ItemName.heatprotectsuit, player)
    )


def can_tlotn_rb(state: CollectionState, player: int):
    return (
            state.has(ItemName.poisonivy_unlocked, player)
            and char_can_double_jump(state, player)
            and state.has(ItemName.attractsuit, player)
    )


def set_entrance_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.ycbob, player),
             lambda state: state.has(ItemName.ycbob_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.air, player),
             lambda state: state.has(ItemName.air_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tfc, player),
             lambda state: state.has(ItemName.tfc_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.apa, player),
             lambda state: state.has(ItemName.apa_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tfo, player),
             lambda state: level_access_tfo(state, options, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tsga, player),
             lambda state: state.has(ItemName.tsga_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.bbb, player),
             lambda state: state.has(ItemName.bbb_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.utc, player),
             lambda state: state.has(ItemName.utc_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.zc, player),
             lambda state: state.has(ItemName.zc_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.pl, player),
             lambda state: state.has(ItemName.pl_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.jht, player),
             lambda state: level_access_jht(state, options, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.lfabt, player),
             lambda state: state.has(ItemName.lfabt_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.fotb, player),
             lambda state: state.has(ItemName.fotb_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.itdn, player),
             lambda state: state.has(ItemName.itdn_lvl, player))
    set_rule(world.get_entrance(RegionName.bc + " -> " + RegionName.tttot, player),
             lambda state: state.has(ItemName.tttot_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.trmaw, player),
             lambda state: state.has(ItemName.trmaw_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.otr, player),
             lambda state: state.has(ItemName.otr_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.gf, player),
             lambda state: state.has(ItemName.gf_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.aet, player),
             lambda state: state.has(ItemName.aet_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.bb, player),
             lambda state: state.has(ItemName.bb_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.rtd, player),
             lambda state: state.has(ItemName.rtd_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.sts, player),
             lambda state: state.has(ItemName.sts_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.hag, player),
             lambda state: state.has(ItemName.hag_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.adr, player),
             lambda state: state.has(ItemName.adr_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.aw, player),
             lambda state: state.has(ItemName.aw_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.asftc, player),
             lambda state: state.has(ItemName.asftc_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.bbpl, player),
             lambda state: state.has(ItemName.bbpl_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.tjm, player),
             lambda state: state.has(ItemName.tjm_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.tlotn, player),
             lambda state: state.has(ItemName.tlotn_lvl, player))
    set_rule(world.get_entrance(RegionName.aa + " -> " + RegionName.dol, player),
             lambda state: state.has(ItemName.dol_lvl, player))
    # Sub Regions
    set_rule(world.get_entrance(RegionName.ycbob + " -> " + RegionName.ycbobf, player),
             lambda state: free_access_ycbob(state, player))
    set_rule(world.get_entrance(RegionName.air + " -> " + RegionName.airf, player),
             lambda state: free_access_air(state, player))
    set_rule(world.get_entrance(RegionName.tfc + " -> " + RegionName.tfcf, player),
             lambda state: free_access_tfc(state, player))
    set_rule(world.get_entrance(RegionName.apa + " -> " + RegionName.apaf, player),
             lambda state: free_access_apa(state, player))
    set_rule(world.get_entrance(RegionName.tfo + " -> " + RegionName.tfof, player),
             lambda state: free_access_tfo(state, player))
    set_rule(world.get_entrance(RegionName.tsga + " -> " + RegionName.tsgaf, player),
             lambda state: free_access_tsga(state, options, player))
    set_rule(world.get_entrance(RegionName.bbb + " -> " + RegionName.bbbf, player),
             lambda state: free_access_bbb(state, player))
    set_rule(world.get_entrance(RegionName.utc + " -> " + RegionName.utcf, player),
             lambda state: free_access_utc(state, player))
    set_rule(world.get_entrance(RegionName.zc + " -> " + RegionName.zcf, player),
             lambda state: free_access_zc(state, options, player))
    set_rule(world.get_entrance(RegionName.pl + " -> " + RegionName.plf, player),
             lambda state: free_access_pl(state, options, player))
    set_rule(world.get_entrance(RegionName.lfabt + " -> " + RegionName.lfabtf, player),
             lambda state: free_access_lfabt(state, options, player))
    set_rule(world.get_entrance(RegionName.itdn + " -> " + RegionName.itdnf, player),
             lambda state: free_access_itdn(state, options, player))
    set_rule(world.get_entrance(RegionName.tttot + " -> " + RegionName.tttotf, player),
             lambda state: free_access_tttot(state, player))
    set_rule(world.get_entrance(RegionName.trmaw + " -> " + RegionName.trmawf, player),
             lambda state: free_access_trmaw(state, player))
    set_rule(world.get_entrance(RegionName.otr + " -> " + RegionName.otrf, player),
             lambda state: free_access_otr(state, player))
    set_rule(world.get_entrance(RegionName.gf + " -> " + RegionName.gff, player),
             lambda state: free_access_gf(state, player))
    set_rule(world.get_entrance(RegionName.bb + " -> " + RegionName.bbf, player),
             lambda state: free_access_bb(state, player))
    set_rule(world.get_entrance(RegionName.rtd + " -> " + RegionName.rtdf, player),
             lambda state: free_access_rtd(state, player))
    set_rule(world.get_entrance(RegionName.sts + " -> " + RegionName.stsf, player),
             lambda state: free_access_sts(state, player))
    set_rule(world.get_entrance(RegionName.hag + " -> " + RegionName.hagf, player),
             lambda state: free_access_hag(state, player))
    set_rule(world.get_entrance(RegionName.adr + " -> " + RegionName.adrf, player),
             lambda state: free_access_adr(state, player))
    set_rule(world.get_entrance(RegionName.aw + " -> " + RegionName.awf, player),
             lambda state: free_access_aw(state, player))
    set_rule(world.get_entrance(RegionName.asftc + " -> " + RegionName.asftcf, player),
             lambda state: free_access_asftc(state, player))
    set_rule(world.get_entrance(RegionName.bbpl + " -> " + RegionName.bbplf, player),
             lambda state: free_access_bbpl(state, player))
    set_rule(world.get_entrance(RegionName.tjm + " -> " + RegionName.tjmf, player),
             lambda state: free_access_tjm(state, player))
    set_rule(world.get_entrance(RegionName.tlotn + " -> " + RegionName.tlotnf, player),
             lambda state: free_access_tlotn(state, player))
    set_rule(world.get_entrance(RegionName.dol + " -> " + RegionName.dolf, player),
             lambda state: free_access_dol(state, player))


def set_level_beaten_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_location(LocationName.ycbob_beat, player), lambda state: can_beat_ycbob(state, options, player))
    set_rule(world.get_location(LocationName.air_beat, player), lambda state: can_beat_air(state, options, player))
    # Two-Face Chase can be beaten in story
    set_rule(world.get_location(LocationName.apa_beat, player), lambda state: can_beat_apa(state, player))
    set_rule(world.get_location(LocationName.tfo_beat, player), lambda state: can_beat_tfo(state, options, player))
    set_rule(world.get_location(LocationName.tsga_beat, player), lambda state: can_beat_tsga(state, options, player))
    # Batboat Battle can be beaten in story
    set_rule(world.get_location(LocationName.utc_beat, player), lambda state: can_beat_utc(state, options, player))
    set_rule(world.get_location(LocationName.zc_beat, player), lambda state: can_beat_zc(state, options, player))
    set_rule(world.get_location(LocationName.pl_beat, player), lambda state: can_beat_pl(state, options, player))
    set_rule(world.get_location(LocationName.jht_beat, player), lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_beat, player), lambda state: can_beat_lfabt(state, options, player))
    # Flight of the Bat can be beaten in story
    set_rule(world.get_location(LocationName.itdn_beat, player), lambda state: can_beat_itdn(state, options, player))
    set_rule(world.get_location(LocationName.tttot_beat, player), lambda state: can_beat_tttot(state, options, player))
    # All Villain Levels can be beaten in story


def set_minikit_rules(world: MultiWorld, options: LB1Options, player: int):
    # YCBOB Minikits 1 & 2 can be done in story for free
    set_rule(world.get_location(LocationName.ycbob_min3, player), lambda state: can_ycbob_min3(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min4, player), lambda state: can_ycbob_min4(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min5, player), lambda state: can_ycbob_min5(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min6, player), lambda state: can_ycbob_min6(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min7, player), lambda state: can_ycbob_min7(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min8, player), lambda state: can_ycbob_min8(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min9, player), lambda state: can_ycbob_min9(state, options, player))
    set_rule(world.get_location(LocationName.ycbob_min10, player),
             lambda state: can_ycbob_min10(state, options, player))
    # AIR Minikit 3 can be done in story for free
    set_rule(world.get_location(LocationName.air_min1, player), lambda state: can_air_min1(state, options, player))
    set_rule(world.get_location(LocationName.air_min2, player), lambda state: can_air_min2(state, options, player))
    set_rule(world.get_location(LocationName.air_min4, player), lambda state: can_air_min4(state, options, player))
    set_rule(world.get_location(LocationName.air_min5, player), lambda state: can_air_min5(state, options, player))
    set_rule(world.get_location(LocationName.air_min6, player), lambda state: can_air_min6(state, options, player))
    set_rule(world.get_location(LocationName.air_min7, player), lambda state: can_air_min7(state, options, player))
    set_rule(world.get_location(LocationName.air_min8, player), lambda state: can_air_min8(state, options, player))
    set_rule(world.get_location(LocationName.air_min9, player), lambda state: can_air_min9(state, options, player))
    set_rule(world.get_location(LocationName.air_min10, player), lambda state: can_air_min10(state, options, player))
    # TFC Minikits 1, 2, 3, 4, 5, 6, 9 can be done in story for free
    set_rule(world.get_location(LocationName.tfc_min7, player), lambda state: can_tfc_min7(state, player))
    set_rule(world.get_location(LocationName.tfc_min8, player), lambda state: can_tfc_min8(state, player))
    set_rule(world.get_location(LocationName.tfc_min10, player), lambda state: can_tfc_min10(state, player))
    # APA Minikit 1 can be done in story for free
    set_rule(world.get_location(LocationName.apa_min2, player), lambda state: can_apa_min2(state, options, player))
    set_rule(world.get_location(LocationName.apa_min3, player), lambda state: can_apa_min3(state, options, player))
    set_rule(world.get_location(LocationName.apa_min4, player), lambda state: can_apa_min4(state, options, player))
    set_rule(world.get_location(LocationName.apa_min5, player), lambda state: can_apa_min5(state, player))
    set_rule(world.get_location(LocationName.apa_min6, player), lambda state: can_apa_min6(state, options, player))
    set_rule(world.get_location(LocationName.apa_min7, player), lambda state: can_apa_min7(state, options, player))
    set_rule(world.get_location(LocationName.apa_min8, player), lambda state: can_apa_min8(state, options, player))
    set_rule(world.get_location(LocationName.apa_min9, player), lambda state: can_apa_min9(state, player))
    set_rule(world.get_location(LocationName.apa_min10, player), lambda state: can_apa_min10(state, player))
    # TFO Minikits 1, 2, 3 can be done with region access in story
    set_rule(world.get_location(LocationName.tfo_min4, player), lambda state: can_tfo_min4(state, options, player))
    set_rule(world.get_location(LocationName.tfo_min5, player), lambda state: can_tfo_min5(state, options, player))
    set_rule(world.get_location(LocationName.tfo_min6, player), lambda state: can_tfo_min6(state, options, player))
    set_rule(world.get_location(LocationName.tfo_min7, player), lambda state: can_tfo_min7(state, options, player))
    set_rule(world.get_location(LocationName.tfo_min8, player), lambda state: can_tfo_min8(state, options, player))
    set_rule(world.get_location(LocationName.tfo_min9, player), lambda state: can_tfo_min9(state, options, player))
    set_rule(world.get_location(LocationName.tfo_min10, player), lambda state: can_tfo_min10(state, options, player))
    # TSGA Minikit 6 can be done in story (with Glide/Magnet which is region access logic)
    set_rule(world.get_location(LocationName.tsga_min1, player), lambda state: can_tsga_min1(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min2, player), lambda state: can_tsga_min2(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min3, player), lambda state: can_tsga_min3(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min4, player), lambda state: can_tsga_min4(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min5, player), lambda state: can_tsga_min5(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min7, player), lambda state: can_tsga_min7(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min8, player), lambda state: can_tsga_min8(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min9, player), lambda state: can_tsga_min9(state, options, player))
    set_rule(world.get_location(LocationName.tsga_min10, player), lambda state: can_tsga_min10(state, options, player))
    # BBB Minikits 1, 2, 4, 7, 8 can be done in story
    set_rule(world.get_location(LocationName.bbb_min3, player), lambda state: can_bbb_min3(state, player))
    set_rule(world.get_location(LocationName.bbb_min5, player), lambda state: can_bbb_min5(state, player))
    set_rule(world.get_location(LocationName.bbb_min6, player), lambda state: can_bbb_min6(state, player))
    set_rule(world.get_location(LocationName.bbb_min9, player), lambda state: can_bbb_min9(state, player))
    set_rule(world.get_location(LocationName.bbb_min10, player), lambda state: can_bbb_min10(state, player))
    # UTC Minikits
    set_rule(world.get_location(LocationName.utc_min1, player), lambda state: can_utc_min1(state, options, player))
    set_rule(world.get_location(LocationName.utc_min2, player), lambda state: can_utc_min2(state, options, player))
    set_rule(world.get_location(LocationName.utc_min3, player), lambda state: can_utc_min3(state, options, player))
    set_rule(world.get_location(LocationName.utc_min4, player), lambda state: can_utc_min4(state, options, player))
    set_rule(world.get_location(LocationName.utc_min5, player), lambda state: can_utc_min5(state, options, player))
    set_rule(world.get_location(LocationName.utc_min6, player), lambda state: can_utc_min6(state, options, player))
    set_rule(world.get_location(LocationName.utc_min7, player), lambda state: can_utc_min7(state, options, player))
    set_rule(world.get_location(LocationName.utc_min8, player), lambda state: can_utc_min8(state, options, player))
    set_rule(world.get_location(LocationName.utc_min9, player), lambda state: can_utc_min9(state, options, player))
    set_rule(world.get_location(LocationName.utc_min10, player), lambda state: can_utc_min10(state, options, player))
    # ZC Minikit 7 can be done with region access
    set_rule(world.get_location(LocationName.zc_min1, player), lambda state: can_zc_min1(state, options, player))
    set_rule(world.get_location(LocationName.zc_min2, player), lambda state: can_zc_min2(state, options, player))
    set_rule(world.get_location(LocationName.zc_min3, player), lambda state: can_zc_min3(state, options, player))
    set_rule(world.get_location(LocationName.zc_min4, player), lambda state: can_zc_min4(state, options, player))
    set_rule(world.get_location(LocationName.zc_min5, player), lambda state: can_zc_min5(state, options, player))
    set_rule(world.get_location(LocationName.zc_min6, player), lambda state: can_zc_min6(state, options, player))
    set_rule(world.get_location(LocationName.zc_min8, player), lambda state: can_zc_min8(state, options, player))
    set_rule(world.get_location(LocationName.zc_min9, player), lambda state: can_zc_min9(state, options, player))
    set_rule(world.get_location(LocationName.zc_min10, player), lambda state: can_zc_min10(state, options, player))
    # PL Minikits 4, 5, 6, 9 can be done with region access
    set_rule(world.get_location(LocationName.pl_min1, player), lambda state: can_pl_min1(state, options, player))
    set_rule(world.get_location(LocationName.pl_min2, player), lambda state: can_pl_min2(state, options, player))
    set_rule(world.get_location(LocationName.pl_min3, player), lambda state: can_pl_min3(state, options, player))
    set_rule(world.get_location(LocationName.pl_min7, player), lambda state: can_pl_min7(state, player))
    set_rule(world.get_location(LocationName.pl_min8, player), lambda state: can_pl_min8(state, player))
    set_rule(world.get_location(LocationName.pl_min10, player), lambda state: can_pl_min10(state, player))
    # JHT Minikit 2 can be done with region access
    set_rule(world.get_location(LocationName.jht_min1, player), lambda state: can_jht_min1(state, options, player))
    set_rule(world.get_location(LocationName.jht_min3, player), lambda state: can_jht_min3(state, options, player))
    set_rule(world.get_location(LocationName.jht_min4, player), lambda state: can_jht_min4(state, options, player))
    set_rule(world.get_location(LocationName.jht_min5, player), lambda state: can_jht_min5(state, options, player))
    set_rule(world.get_location(LocationName.jht_min6, player), lambda state: can_jht_min6(state, options, player))
    set_rule(world.get_location(LocationName.jht_min7, player), lambda state: can_jht_min7(state, options, player))
    set_rule(world.get_location(LocationName.jht_min8, player), lambda state: can_jht_min8(state, options, player))
    set_rule(world.get_location(LocationName.jht_min9, player), lambda state: can_jht_min9(state, options, player))
    set_rule(world.get_location(LocationName.jht_min10, player), lambda state: can_jht_min10(state, options, player))
    # LFABT Minikits
    set_rule(world.get_location(LocationName.lfabt_min1, player), lambda state: can_lfabt_min1(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min2, player), lambda state: can_lfabt_min2(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min3, player), lambda state: can_lfabt_min3(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min4, player), lambda state: can_lfabt_min4(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min5, player), lambda state: can_lfabt_min5(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min6, player), lambda state: can_lfabt_min6(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min7, player), lambda state: can_lfabt_min7(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min8, player), lambda state: can_lfabt_min8(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min9, player), lambda state: can_lfabt_min9(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_min10, player),
             lambda state: can_lfabt_min10(state, options, player))
    # FOTB Minikits 1, 2, 3, 4, 5, 6, 8, 10 can be done in story
    set_rule(world.get_location(LocationName.fotb_min7, player), lambda state: can_fotb_min7(state, player))
    set_rule(world.get_location(LocationName.fotb_min9, player), lambda state: can_fotb_min9(state, player))
    # ITDN Minikits
    set_rule(world.get_location(LocationName.itdn_min1, player), lambda state: can_itdn_min1(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min2, player), lambda state: can_itdn_min2(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min3, player), lambda state: can_itdn_min3(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min4, player), lambda state: can_itdn_min4(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min5, player), lambda state: can_itdn_min5(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min6, player), lambda state: can_itdn_min6(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min7, player), lambda state: can_itdn_min7(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min8, player), lambda state: can_itdn_min8(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min9, player), lambda state: can_itdn_min9(state, options, player))
    set_rule(world.get_location(LocationName.itdn_min10, player), lambda state: can_itdn_min10(state, options, player))
    # TTTOT Minikits 2, 7, 8 can be done with region access
    set_rule(world.get_location(LocationName.tttot_min1, player), lambda state: can_tttot_min1(state, options, player))
    set_rule(world.get_location(LocationName.tttot_min3, player), lambda state: can_tttot_min3(state, options, player))
    set_rule(world.get_location(LocationName.tttot_min4, player), lambda state: can_tttot_min4(state, options, player))
    set_rule(world.get_location(LocationName.tttot_min5, player), lambda state: can_tttot_min5(state, options, player))
    set_rule(world.get_location(LocationName.tttot_min6, player), lambda state: can_tttot_min6(state, options, player))
    set_rule(world.get_location(LocationName.tttot_min9, player), lambda state: can_tttot_min9(state, options, player))
    set_rule(world.get_location(LocationName.tttot_min10, player),
             lambda state: can_tttot_min10(state, options, player))
    # TRMAW Minikits 1-3, 5, 7, 8, 10 can be done in story
    set_rule(world.get_location(LocationName.trmaw_min4, player), lambda state: can_trmaw_min4(state, player))
    set_rule(world.get_location(LocationName.trmaw_min6, player), lambda state: can_trmaw_min6_and_9(state, player))
    set_rule(world.get_location(LocationName.trmaw_min9, player), lambda state: can_trmaw_min6_and_9(state, player))
    # OTR Minikits 1, 3, 6, 10 can be done in story
    set_rule(world.get_location(LocationName.otr_min2, player), lambda state: can_otr_min2(state, player))
    set_rule(world.get_location(LocationName.otr_min4, player), lambda state: can_otr_min4(state, player))
    set_rule(world.get_location(LocationName.otr_min5, player), lambda state: can_otr_min5(state, player))
    set_rule(world.get_location(LocationName.otr_min7, player), lambda state: can_otr_min7(state, player))
    set_rule(world.get_location(LocationName.otr_min8, player), lambda state: can_otr_min8(state, player))
    set_rule(world.get_location(LocationName.otr_min9, player), lambda state: can_otr_min9(state, player))
    # GF Minikit 3 can be done in story
    set_rule(world.get_location(LocationName.gf_min1, player), lambda state: can_gf_min1(state, player))
    set_rule(world.get_location(LocationName.gf_min2, player), lambda state: can_gf_min2(state, player))
    set_rule(world.get_location(LocationName.gf_min4, player), lambda state: can_gf_min4(state, player))
    set_rule(world.get_location(LocationName.gf_min5, player), lambda state: can_gf_min5(state, player))
    set_rule(world.get_location(LocationName.gf_min6, player), lambda state: can_gf_min6(state, player))
    set_rule(world.get_location(LocationName.gf_min7, player), lambda state: can_gf_min7(state, player))
    set_rule(world.get_location(LocationName.gf_min8, player), lambda state: can_gf_min8(state, player))
    set_rule(world.get_location(LocationName.gf_min9, player), lambda state: can_gf_min9(state, player))
    set_rule(world.get_location(LocationName.gf_min10, player), lambda state: can_gf_min10(state, player))
    # AET Minikits 6 & 10 can be done in story
    set_rule(world.get_location(LocationName.aet_min1, player), lambda state: can_aet_min1(state, player))
    set_rule(world.get_location(LocationName.aet_min2, player), lambda state: can_aet_min2(state, player))
    set_rule(world.get_location(LocationName.aet_min3, player), lambda state: can_aet_min3(state, player))
    set_rule(world.get_location(LocationName.aet_min4, player), lambda state: can_aet_min4(state, player))
    set_rule(world.get_location(LocationName.aet_min5, player), lambda state: can_aet_min5(state, player))
    set_rule(world.get_location(LocationName.aet_min7, player), lambda state: can_aet_min7(state, player))
    set_rule(world.get_location(LocationName.aet_min8, player), lambda state: can_aet_min8(state, player))
    set_rule(world.get_location(LocationName.aet_min9, player), lambda state: can_aet_min9(state, player))
    # BB Minikit 1 can be done in story & 3 can be done in freeplay with batman & region access
    set_rule(world.get_location(LocationName.bb_min2, player), lambda state: can_bb_min2(state, player))
    set_rule(world.get_location(LocationName.bb_min4, player), lambda state: can_bb_min4(state, player))
    set_rule(world.get_location(LocationName.bb_min5, player), lambda state: can_bb_min5(state, player))
    set_rule(world.get_location(LocationName.bb_min6, player), lambda state: can_bb_min6(state, player))
    set_rule(world.get_location(LocationName.bb_min7, player), lambda state: can_bb_min7(state, player))
    set_rule(world.get_location(LocationName.bb_min8, player), lambda state: can_bb_min8(state, player))
    set_rule(world.get_location(LocationName.bb_min9, player), lambda state: can_bb_min9(state, player))
    set_rule(world.get_location(LocationName.bb_min10, player), lambda state: can_bb_min10(state, player))
    # RTD Minikits 3, 4, 6, 8, 10 can be done in story
    set_rule(world.get_location(LocationName.rtd_min1, player), lambda state: can_rtd_min1(state, player))
    set_rule(world.get_location(LocationName.rtd_min2, player), lambda state: can_rtd_min2(state, player))
    set_rule(world.get_location(LocationName.rtd_min5, player), lambda state: can_rtd_min5(state, player))
    set_rule(world.get_location(LocationName.rtd_min7, player), lambda state: can_rtd_min7(state, player))
    set_rule(world.get_location(LocationName.rtd_min9, player), lambda state: can_rtd_min9(state, player))
    # STS Minikits 2, 4, 5, 8 can be done in story
    set_rule(world.get_location(LocationName.sts_min1, player), lambda state: can_sts_min1(state, player))
    set_rule(world.get_location(LocationName.sts_min3, player), lambda state: can_sts_min3(state, player))
    set_rule(world.get_location(LocationName.sts_min6, player), lambda state: can_sts_min6(state, player))
    set_rule(world.get_location(LocationName.sts_min7, player), lambda state: can_sts_min7(state, player))
    set_rule(world.get_location(LocationName.sts_min9, player), lambda state: can_sts_min9(state, player))
    set_rule(world.get_location(LocationName.sts_min10, player), lambda state: can_sts_min10(state, player))
    # HAG Minikits 1, 2, 4-7, 9 can be done in story
    set_rule(world.get_location(LocationName.hag_min3, player), lambda state: can_hag_min3(state, player))
    set_rule(world.get_location(LocationName.hag_min8, player), lambda state: can_hag_min8(state, player))
    set_rule(world.get_location(LocationName.hag_min10, player), lambda state: can_hag_min10(state, player))
    # ADR Minikits 1, 4, 8, 10 can be done in story
    set_rule(world.get_location(LocationName.adr_min2, player), lambda state: can_adr_min2(state, player))
    set_rule(world.get_location(LocationName.adr_min3, player), lambda state: can_adr_min3(state, player))
    set_rule(world.get_location(LocationName.adr_min5, player), lambda state: can_adr_min5(state, player))
    set_rule(world.get_location(LocationName.adr_min6, player), lambda state: can_adr_min6(state, player))
    set_rule(world.get_location(LocationName.adr_min7, player), lambda state: can_adr_min7(state, player))
    set_rule(world.get_location(LocationName.adr_min9, player), lambda state: can_adr_min9(state, player))
    # AW Minikit 7 can be done in story
    set_rule(world.get_location(LocationName.aw_min1, player), lambda state: can_aw_min1(state, player))
    set_rule(world.get_location(LocationName.aw_min2, player), lambda state: can_aw_min2(state, player))
    set_rule(world.get_location(LocationName.aw_min3, player), lambda state: can_aw_min3(state, player))
    set_rule(world.get_location(LocationName.aw_min4, player), lambda state: can_aw_min4(state, player))
    set_rule(world.get_location(LocationName.aw_min5, player), lambda state: can_aw_min5(state, player))
    set_rule(world.get_location(LocationName.aw_min6, player), lambda state: can_aw_min6(state, player))
    set_rule(world.get_location(LocationName.aw_min8, player), lambda state: can_aw_min8(state, player))
    set_rule(world.get_location(LocationName.aw_min9, player), lambda state: can_aw_min9(state, player))
    set_rule(world.get_location(LocationName.aw_min10, player), lambda state: can_aw_min10(state, player))
    # ASFTC Minikit 6 and 10 can be done in story
    set_rule(world.get_location(LocationName.asftc_min1, player), lambda state: can_asftc_min1(state, player))
    set_rule(world.get_location(LocationName.asftc_min2, player), lambda state: can_asftc_min2(state, player))
    set_rule(world.get_location(LocationName.asftc_min3, player), lambda state: can_asftc_min3(state, player))
    set_rule(world.get_location(LocationName.asftc_min4, player), lambda state: can_asftc_min4(state, player))
    set_rule(world.get_location(LocationName.asftc_min5, player), lambda state: can_asftc_min5(state, player))
    set_rule(world.get_location(LocationName.asftc_min7, player), lambda state: can_asftc_min7(state, player))
    set_rule(world.get_location(LocationName.asftc_min8, player), lambda state: can_asftc_min8(state, player))
    set_rule(world.get_location(LocationName.asftc_min9, player), lambda state: can_asftc_min9(state, player))
    # BBPL Minikits can be done in story or with freeplay region access
    # TJM Minikits 1, 2, and 10 can be done in story
    set_rule(world.get_location(LocationName.tjm_min3, player), lambda state: can_tjm_min3(state, player))
    set_rule(world.get_location(LocationName.tjm_min4, player), lambda state: can_tjm_min4(state, player))
    set_rule(world.get_location(LocationName.tjm_min5, player), lambda state: can_tjm_min5(state, player))
    set_rule(world.get_location(LocationName.tjm_min6, player), lambda state: can_tjm_min6(state, player))
    set_rule(world.get_location(LocationName.tjm_min7, player), lambda state: can_tjm_min7(state, player))
    set_rule(world.get_location(LocationName.tjm_min8, player), lambda state: can_tjm_min8(state, player))
    set_rule(world.get_location(LocationName.tjm_min9, player), lambda state: can_tjm_min9(state, player))
    # TLOTN Minikits 6, 7, 8 can be done in story
    set_rule(world.get_location(LocationName.tlotn_min1, player), lambda state: can_tlotn_min1(state, player))
    set_rule(world.get_location(LocationName.tlotn_min2, player), lambda state: can_tlotn_min2(state, player))
    set_rule(world.get_location(LocationName.tlotn_min3, player), lambda state: can_tlotn_min3(state, player))
    set_rule(world.get_location(LocationName.tlotn_min4, player), lambda state: can_tlotn_min4(state, player))
    set_rule(world.get_location(LocationName.tlotn_min5, player), lambda state: can_tlotn_min5(state, player))
    set_rule(world.get_location(LocationName.tlotn_min9, player), lambda state: can_tlotn_min9(state, player))
    set_rule(world.get_location(LocationName.tlotn_min10, player), lambda state: can_tlotn_min10(state, player))
    # DOL Minikit 9 can be done in story & 6 can be done with region access
    set_rule(world.get_location(LocationName.dol_min1, player), lambda state: can_dol_min1(state, player))
    set_rule(world.get_location(LocationName.dol_min2, player), lambda state: can_dol_min2(state, player))
    set_rule(world.get_location(LocationName.dol_min3, player), lambda state: can_dol_min3(state, player))
    set_rule(world.get_location(LocationName.dol_min4, player), lambda state: can_dol_min4(state, player))
    set_rule(world.get_location(LocationName.dol_min5, player), lambda state: can_dol_min5(state, player))
    set_rule(world.get_location(LocationName.dol_min7, player), lambda state: can_dol_min7(state, player))
    set_rule(world.get_location(LocationName.dol_min8, player), lambda state: can_dol_min8(state, player))
    set_rule(world.get_location(LocationName.dol_min10, player), lambda state: can_dol_min10(state, player))


def set_host_rules(world: MultiWorld, options: LB1Options, player: int):
    # You Can Bank of Batman host can be obtained during story for free
    set_rule(world.get_location(LocationName.air_host, player), lambda state: can_air_host(state, options, player))
    # Two-Face Chase does not have host
    set_rule(world.get_location(LocationName.apa_host, player), lambda state: can_apa_host(state, player))
    set_rule(world.get_location(LocationName.tfo_host, player), lambda state: can_tfo_host(state, options, player))
    # There She Goes Again host can be obtained with Region Access
    # Batboat Battle does not have host
    set_rule(world.get_location(LocationName.utc_host, player), lambda state: can_utc_host(state, options, player))
    set_rule(world.get_location(LocationName.zc_host, player), lambda state: can_zc_host(state, options, player))
    # Penguin's Lair host can be done with Region Access
    set_rule(world.get_location(LocationName.jht_host, player), lambda state: can_jht_host(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_host, player), lambda state: can_lfabt_host(state, options, player))
    # Flight of the Bat does not have host
    set_rule(world.get_location(LocationName.itdn_host, player), lambda state: can_itdn_host(state, options, player))
    # To the Top of the Tower host can be obtained during story and for free
    set_rule(world.get_location(LocationName.trmaw_host, player), lambda state: can_trmaw_host(state, player))
    set_rule(world.get_location(LocationName.otr_host, player), lambda state: can_otr_host(state, player))
    set_rule(world.get_location(LocationName.gf_host, player), lambda state: can_gf_host(state, player))
    set_rule(world.get_location(LocationName.aet_host, player), lambda state: can_aet_host(state, player))
    set_rule(world.get_location(LocationName.bb_host, player), lambda state: can_bb_host(state, player))
    set_rule(world.get_location(LocationName.rtd_host, player), lambda state: can_rtd_host(state, player))
    set_rule(world.get_location(LocationName.sts_host, player), lambda state: can_sts_host(state, player))
    # Harbouring a Grudge does not have host
    set_rule(world.get_location(LocationName.adr_host, player), lambda state: can_adr_host(state, player))
    set_rule(world.get_location(LocationName.aw_host, player), lambda state: can_aw_host(state, player))
    set_rule(world.get_location(LocationName.asftc_host, player), lambda state: can_asftc_host(state, player))
    # Biplane Blast does not have host
    set_rule(world.get_location(LocationName.tjm_host, player), lambda state: can_tjm_host(state, player))
    set_rule(world.get_location(LocationName.tlotn_host, player), lambda state: can_tlotn_host(state, player))
    set_rule(world.get_location(LocationName.dol_host, player), lambda state: can_dol_host(state, player))


# Current logic implementation is that multiplier/can beat level. In separate function since always score multiply \
# is a starting item
def set_true_status_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_location(LocationName.ycbob_ts, player), lambda state: can_beat_ycbob(state, options, player))
    set_rule(world.get_location(LocationName.air_ts, player), lambda state: can_beat_air(state, options, player))
    # Two-Face Chase can be beaten in story
    set_rule(world.get_location(LocationName.apa_ts, player), lambda state: can_beat_apa(state, player))
    set_rule(world.get_location(LocationName.tfo_ts, player), lambda state: can_beat_tfo(state, options, player))
    set_rule(world.get_location(LocationName.tsga_ts, player), lambda state: can_beat_tsga(state, options, player))
    # Batboat Battle can be beaten in story
    set_rule(world.get_location(LocationName.utc_ts, player), lambda state: can_beat_utc(state, options, player))
    set_rule(world.get_location(LocationName.zc_ts, player), lambda state: can_beat_zc(state, options, player))
    set_rule(world.get_location(LocationName.pl_ts, player), lambda state: can_beat_pl(state, options, player))
    set_rule(world.get_location(LocationName.jht_ts, player), lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_ts, player), lambda state: can_beat_lfabt(state, options, player))
    # Flight of the Bat can be beaten in story
    set_rule(world.get_location(LocationName.itdn_ts, player), lambda state: can_beat_itdn(state, options, player))
    set_rule(world.get_location(LocationName.tttot_ts, player), lambda state: can_beat_tttot(state, options, player))
    # All Villain Levels can be beaten in story


def set_red_brick_location_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_location(LocationName.ycbob_rb, player), lambda state: can_ycbob_rb(state, options, player))
    set_rule(world.get_location(LocationName.air_rb, player), lambda state: can_air_rb(state, options, player))
    # Two-Face Chase Red Brick can be obtained in story
    set_rule(world.get_location(LocationName.apa_rb, player), lambda state: can_apa_rb(state, options, player))
    set_rule(world.get_location(LocationName.tfo_rb, player), lambda state: can_tfo_rb(state, options, player))
    set_rule(world.get_location(LocationName.tsga_rb, player), lambda state: can_tsga_rb(state, options, player))
    set_rule(world.get_location(LocationName.bbb_rb, player), lambda state: can_bbb_rb(state, player))
    set_rule(world.get_location(LocationName.utc_rb, player), lambda state: can_utc_rb(state, options, player))
    set_rule(world.get_location(LocationName.zc_rb, player), lambda state: can_zc_rb(state, options, player))
    set_rule(world.get_location(LocationName.pl_rb, player), lambda state: can_pl_rb(state, player))
    set_rule(world.get_location(LocationName.jht_rb, player), lambda state: can_jht_rb(state, options, player))
    set_rule(world.get_location(LocationName.lfabt_rb, player), lambda state: can_lfabt_rb(state, options, player))
    set_rule(world.get_location(LocationName.fotb_rb, player), lambda state: can_fotb_rb(state, player))
    set_rule(world.get_location(LocationName.itdn_rb, player), lambda state: can_itdn_rb(state, options, player))
    set_rule(world.get_location(LocationName.tttot_rb, player), lambda state: can_tttot_rb(state, options, player))
    set_rule(world.get_location(LocationName.trmaw_rb, player), lambda state: can_trmaw_rb(state, player))
    set_rule(world.get_location(LocationName.otr_rb, player), lambda state: can_otr_rb(state, player))
    set_rule(world.get_location(LocationName.gf_rb, player), lambda state: can_gf_rb(state, player))
    set_rule(world.get_location(LocationName.aet_rb, player), lambda state: can_aet_rb(state, player))
    set_rule(world.get_location(LocationName.bb_rb, player), lambda state: can_bb_rb(state, player))
    set_rule(world.get_location(LocationName.rtd_rb, player), lambda state: can_rtd_rb(state, player))
    set_rule(world.get_location(LocationName.sts_rb, player), lambda state: can_sts_rb(state, player))
    set_rule(world.get_location(LocationName.hag_rb, player), lambda state: can_hag_rb(state, player))
    set_rule(world.get_location(LocationName.adr_rb, player), lambda state: can_adr_rb(state, player))
    set_rule(world.get_location(LocationName.aw_rb, player), lambda state: can_aw_rb(state, player))
    set_rule(world.get_location(LocationName.asftc_rb, player), lambda state: can_asftc_rb(state, player))
    # BBPL Red Brick can be obtained in story
    set_rule(world.get_location(LocationName.tjm_rb, player), lambda state: can_tjm_rb(state, player))
    set_rule(world.get_location(LocationName.tlotn_rb, player), lambda state: can_tlotn_rb(state, player))
    # DOL Red Brick can be obtained in freeplay with nothing additional


def set_red_brick_purchase_rules(world: MultiWorld, player: int):
    set_rule(world.get_location(LocationName.scorex2, player), lambda state: state.has(ItemName.trmaw_rbc, player))
    set_rule(world.get_location(LocationName.scorex4, player), lambda state: state.has(ItemName.otr_rbc, player))
    set_rule(world.get_location(LocationName.scorex6, player), lambda state: state.has(ItemName.gf_rbc, player))
    set_rule(world.get_location(LocationName.scorex8, player), lambda state: state.has(ItemName.aet_rbc, player))
    set_rule(world.get_location(LocationName.scorex10, player), lambda state: state.has(ItemName.bb_rbc, player))
    set_rule(world.get_location(LocationName.studmagnet, player), lambda state: state.has(ItemName.rtd_rbc, player))
    set_rule(world.get_location(LocationName.charstuds, player), lambda state: state.has(ItemName.sts_rbc, player))
    set_rule(world.get_location(LocationName.minikitdetect, player), lambda state: state.has(ItemName.hag_rbc, player))
    set_rule(world.get_location(LocationName.pwrbrickdetect, player), lambda state: state.has(ItemName.adr_rbc, player))
    set_rule(world.get_location(LocationName.alwaysscore, player), lambda state: state.has(ItemName.aw_rbc, player))
    set_rule(world.get_location(LocationName.fastbuild, player), lambda state: state.has(ItemName.asftc_rbc, player))
    set_rule(world.get_location(LocationName.immunefreeze, player), lambda state: state.has(ItemName.bbpl_rbc, player))
    set_rule(world.get_location(LocationName.regenhearts, player), lambda state: state.has(ItemName.tjm_rbc, player))
    set_rule(world.get_location(LocationName.extrahearts, player), lambda state: state.has(ItemName.tlotn_rbc, player))
    set_rule(world.get_location(LocationName.invincibility, player), lambda state: state.has(ItemName.dol_rbc, player))
    set_rule(world.get_location(LocationName.fastgrapple, player), lambda state: state.has(ItemName.ycbob_rbc, player))
    set_rule(world.get_location(LocationName.fastbatarang, player), lambda state: state.has(ItemName.air_rbc, player))
    set_rule(world.get_location(LocationName.moretargets, player), lambda state: state.has(ItemName.tfc_rbc, player))
    set_rule(world.get_location(LocationName.flamingbata, player), lambda state: state.has(ItemName.apa_rbc, player))
    set_rule(world.get_location(LocationName.slam, player), lambda state: state.has(ItemName.tfo_rbc, player))
    set_rule(world.get_location(LocationName.moredet, player), lambda state: state.has(ItemName.tsga_rbc, player))
    set_rule(world.get_location(LocationName.armorplating, player), lambda state: state.has(ItemName.bbb_rbc, player))
    set_rule(world.get_location(LocationName.sonicpain, player), lambda state: state.has(ItemName.utc_rbc, player))
    set_rule(world.get_location(LocationName.areaeffect, player), lambda state: state.has(ItemName.zc_rbc, player))
    set_rule(world.get_location(LocationName.bats, player), lambda state: state.has(ItemName.pl_rbc, player))
    set_rule(world.get_location(LocationName.freezebatarang, player), lambda state: state.has(ItemName.jht_rbc, player))
    set_rule(world.get_location(LocationName.decoy, player), lambda state: state.has(ItemName.lfabt_rbc, player))
    set_rule(world.get_location(LocationName.fastwalk, player), lambda state: state.has(ItemName.fotb_rbc, player))
    set_rule(world.get_location(LocationName.fasterpieces, player), lambda state: state.has(ItemName.itdn_rbc, player))
    set_rule(world.get_location(LocationName.piecedetect, player), lambda state: state.has(ItemName.tttot_rbc, player))


def set_rules(world: MultiWorld, options: LB1Options, player: int):
    set_entrance_rules(world, options, player)
    set_level_beaten_rules(world, options, player)
    # char rules
    # Hard char Rules
    # Automobile Rules
    # Watercraft Rules
    # aircraft Rules
    # Suit Rules
    if options.minikit_sanity == 1:
        set_minikit_rules(world, options, player)
    set_host_rules(world, options, player)
    if options.true_status_sanity == 1:
        set_true_status_rules(world, options, player)
    set_red_brick_location_rules(world, options, player)
    set_red_brick_purchase_rules(world, player)

    # Set End Goal
    if options.EndGoal == EndGoal.option_minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)
    elif options.EndGoal == EndGoal.option_levels_beaten:
        world.completion_condition[player] = \
            lambda state: state.has("Level Beaten Token", player, options.levels_to_win)


def set_event_rules(world: MultiWorld, player: int):
    for (name, data) in level_beaten_event_location_table.items():
        event: Location = world.get_location(name, player)
        level_beaten_name = name.removesuffix(" Event")
        set_rule(event, world.get_location(level_beaten_name, player).access_rule)
