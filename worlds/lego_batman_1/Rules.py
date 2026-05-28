from typing import List, Callable

from BaseClasses import MultiWorld, Location
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import CollectionState

from .Locations import event_location_table, purchase_location_table
from .Names import LocationName, ItemName, RegionName
from .Options import LB1Options, EndGoal


# With suits getting pushed back to 0.4, I know this is messy, cause a lot got changed to True instead of evaluating
# the suit, but I will clean it up in 0.4 when we switch to rule builder

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
            True
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
            True
            or state.has(ItemName.killercroc_unlocked, player)
    )


def char_can_explode(state: CollectionState, player: int):
    return (
            True
            or state.has(ItemName.penguin_unlocked, player)
    )


def char_can_techno(state: CollectionState, player: int):
    return (
            True
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


def has_low_multiplier(state: CollectionState, player: int):
    return (
            state.has(ItemName.scorex2_un, player)
            or state.has(ItemName.scorex4_un, player)
            or has_high_multiplier(state, player)
    )


def has_high_multiplier(state: CollectionState, player: int):
    return (
            state.has(ItemName.scorex6_un, player)
            or state.has(ItemName.scorex8_un, player)
            or state.has(ItemName.scorex10_un, player)
            or (state.has(ItemName.scorex2_un, player) and state.has(ItemName.scorex4_un, player))
    )


def has_enough_hostages(state: CollectionState, options: LB1Options, player: int):
    return state.has("UNIQUE_HOSTAGES", player, options.hush_purchase_requirements.value)


def has_enough_minikits(state: CollectionState, options: LB1Options, player: int):
    return state.has("UNIQUE_MINIKITS", player, options.ras_purchase_requirements.value)


def can_purchase_shop_item(
        location: LocationName,
        state: CollectionState,
        options: LB1Options,
        player: int,
        required_items: List[ItemName] = None,
        required_token: ItemName = None,
        extra_conditions: List[Callable[[], bool]] = None
) -> bool:
    required_items = required_items or []
    extra_conditions = extra_conditions or []
    if not (
            has_required_multiplier(location, state, options, player)
            and all(state.has(item, player) for item in required_items)
            and all(cond() for cond in extra_conditions)
    ):
        return False

    if required_token and options.decouple_character_tokens == 1:
        return state.has(required_token, player)

    return True


def has_required_multiplier(location: LocationName, state: CollectionState, options: LB1Options, player: int) -> bool:
    if options.shop_purchases_required_multiplier == 1:
        price = purchase_location_table[location].price
        if price >= options.high_multiplier_minimum.value:
            return has_high_multiplier(state, player)
        elif price >= options.low_multiplier_minimum.value:
            return has_low_multiplier(state, player)
    return True


def can_complete_any_hero_level(state: CollectionState, options: LB1Options, player: int):
    return (
            (state.has(ItemName.ycbob_lvl, player) and can_beat_ycbob(state, options, player))
            or (state.has(ItemName.air_lvl, player) and can_beat_air(state, options, player))
            or state.has(ItemName.tfc_lvl, player)
            or (state.has(ItemName.apa_lvl, player) and can_beat_apa(state, player))
            or (state.has(ItemName.tfo_lvl, player) and can_beat_tfo(state, options, player))
            or (state.has(ItemName.tsga_lvl, player) and can_beat_tsga(state, options, player))
            or state.has(ItemName.bbb_lvl, player)
            or (state.has(ItemName.utc_lvl, player) and can_beat_utc(state, options, player))
            or (state.has(ItemName.zc_lvl, player) and can_beat_zc(state, options, player))
            or (state.has(ItemName.pl_lvl, player) and can_beat_pl(state, options, player))
            or (state.has(ItemName.jht_lvl, player) and can_beat_jht(state, options, player))
            or (state.has(ItemName.lfabt_lvl, player) and can_beat_lfabt(state, options, player))
            or (state.has(ItemName.fotb_lvl, player))
            or (state.has(ItemName.itdn_lvl, player) and can_beat_itdn(state, options, player))
            or (state.has(ItemName.tttot_lvl, player) and can_beat_tttot(state, options, player))
    )


def can_complete_any_hero_episode(state: CollectionState, options: LB1Options, player: int):
    return (
            (state.has(ItemName.ycbob_lvl, player) and can_beat_ycbob(state, options, player)
             and state.has(ItemName.air_lvl, player) and can_beat_air(state, options, player)
             and state.has(ItemName.tfc_lvl, player)
             and state.has(ItemName.apa_lvl, player) and can_beat_apa(state, player)
             and state.has(ItemName.tfo_lvl, player) and can_beat_tfo(state, options, player))
            or (state.has(ItemName.tsga_lvl, player) and can_beat_tsga(state, options, player)
                and state.has(ItemName.bbb_lvl, player)
                and state.has(ItemName.utc_lvl, player) and can_beat_utc(state, options, player)
                and state.has(ItemName.zc_lvl, player) and can_beat_zc(state, options, player)
                and state.has(ItemName.pl_lvl, player) and can_beat_pl(state, options, player))
            or (state.has(ItemName.jht_lvl, player) and can_beat_jht(state, options, player)
                and state.has(ItemName.lfabt_lvl, player) and can_beat_lfabt(state, options, player)
                and state.has(ItemName.fotb_lvl, player)
                and state.has(ItemName.itdn_lvl, player) and can_beat_itdn(state, options, player)
                and state.has(ItemName.tttot_lvl, player) and can_beat_tttot(state, options, player))
    )


def can_complete_all_hero_episode(state: CollectionState, options: LB1Options, player: int):
    return (
            state.has(ItemName.ycbob_lvl, player) and can_beat_ycbob(state, options, player)
            and state.has(ItemName.air_lvl, player) and can_beat_air(state, options, player)
            and state.has(ItemName.tfc_lvl, player)
            and state.has(ItemName.apa_lvl, player) and can_beat_apa(state, player)
            and state.has(ItemName.tfo_lvl, player) and can_beat_tfo(state, options, player)
            and state.has(ItemName.tsga_lvl, player) and can_beat_tsga(state, options, player)
            and state.has(ItemName.bbb_lvl, player)
            and state.has(ItemName.utc_lvl, player) and can_beat_utc(state, options, player)
            and state.has(ItemName.zc_lvl, player) and can_beat_zc(state, options, player)
            and state.has(ItemName.pl_lvl, player) and can_beat_pl(state, options, player)
            and state.has(ItemName.jht_lvl, player) and can_beat_jht(state, options, player)
            and state.has(ItemName.lfabt_lvl, player) and can_beat_lfabt(state, options, player)
            and state.has(ItemName.fotb_lvl, player)
            and state.has(ItemName.itdn_lvl, player) and can_beat_itdn(state, options, player)
            and state.has(ItemName.tttot_lvl, player) and can_beat_tttot(state, options, player)
    )


def can_unlock_two_face(state: CollectionState, player: int):
    return state.has(ItemName.aet_lvl, player) or state.has(ItemName.bb_lvl, player)


def can_unlock_riddler(state: CollectionState, player: int):
    return (
            state.has(ItemName.trmaw_lvl, player) or state.has(ItemName.otr_lvl, player)
            or state.has(ItemName.gf_lvl, player) or state.has(ItemName.aet_lvl, player)
            or state.has(ItemName.bbb_lvl, player)
    )


def can_unlock_catwoman(state: CollectionState, player: int):
    return state.has(ItemName.sts_lvl, player) or state.has(ItemName.aw_lvl, player)


def can_unlock_penguin(state: CollectionState, player: int):
    return (
            state.has(ItemName.rtd_lvl, player) or state.has(ItemName.sts_lvl, player)
            or state.has(ItemName.adr_lvl, player) or state.has(ItemName.aw_lvl, player)
    )


def can_unlock_harley(state: CollectionState, player: int):
    return state.has(ItemName.asftc_lvl, player) or state.has(ItemName.dol_lvl, player)


def can_unlock_joker(state: CollectionState, player: int):
    return (
            state.has(ItemName.asftc_lvl, player) or state.has(ItemName.tjm_lvl, player)
            or state.has(ItemName.tlotn_lvl, player) or state.has(ItemName.dol_lvl, player)
    )


def can_purchase_riddler_goon(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.riddlergoon_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.riddlergoon_token,
        extra_conditions=[
            lambda: (can_beat_ycbob(state, options, player) and state.has(ItemName.ycbob_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_riddler_henchman(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.riddlerhenchman_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.riddlerhenchman_token,
        extra_conditions=[
            lambda: (can_beat_ycbob(state, options, player) and state.has(ItemName.ycbob_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_freeze_girl(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.freezegirl_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.freezegirl_token,
        extra_conditions=[
            lambda: (can_beat_air(state, options, player) and state.has(ItemName.air_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_car(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policecar_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policecar_token,
        extra_conditions=[
            lambda: state.has(ItemName.tfc_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_bike(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policebike_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policebike_token,
        extra_conditions=[
            lambda: state.has(ItemName.tfc_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_van(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policevan_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policevan_token,
        extra_conditions=[
            lambda: state.has(ItemName.tfc_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_joker_van(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.jokervan_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.jokervan_token,
        extra_conditions=[
            lambda: state.has(ItemName.tfc_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_poison_ivy_goon(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.poisonivygoon_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.poisonivygoon_token,
        extra_conditions=[
            lambda: (can_beat_apa(state, player) and state.has(ItemName.apa_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_fishmonger(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.fishmonger_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.fishmonger_token,
        extra_conditions=[
            lambda: (can_beat_tsga(state, options, player) and state.has(ItemName.tsga_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_penguin_goon(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.penguingoon_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.penguingoon_token,
        extra_conditions=[
            lambda: (can_beat_tsga(state, options, player) and state.has(ItemName.tsga_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_penguin_henchman(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.penguinhenchman_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.penguinhenchman_token,
        extra_conditions=[
            lambda: (can_beat_tsga(state, options, player) and state.has(ItemName.tsga_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_robin_sub(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.robinssubmarine_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.robinssubmarine_token,
        extra_conditions=[
            lambda: state.has(ItemName.bbb_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_goon_sub(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.penguingoonsub_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.penguingoonsub_token,
        extra_conditions=[
            lambda: state.has(ItemName.bbb_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_harbour_heli(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.harbourhelicopter_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.harbourhelicopter_token,
        extra_conditions=[
            lambda: state.has(ItemName.bbb_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_zoo_sweeper(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.zoosweeper_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.zoosweeper_token,
        extra_conditions=[
            lambda: (can_beat_zc(state, options, player) and state.has(ItemName.zc_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_manbat(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.manbat_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.manbat_token,
        extra_conditions=[
            lambda: (can_beat_pl(state, options, player) and state.has(ItemName.pl_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_yeti(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.yeti_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.yeti_token,
        extra_conditions=[
            lambda: (can_beat_pl(state, options, player) and state.has(ItemName.pl_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_penguin_minion(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.penguinminion_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.penguinminion_token,
        extra_conditions=[
            lambda: (can_beat_pl(state, options, player) and state.has(ItemName.pl_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_mad_hatter(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.madhatter_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.madhatter_token,
        extra_conditions=[
            lambda: (can_beat_jht(state, options, player) and state.has(ItemName.jht_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_joker_goon(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.jokergoon_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.jokergoon_token,
        extra_conditions=[
            lambda: (can_beat_jht(state, options, player) and state.has(ItemName.jht_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_joker_henchman(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.jokerhenchman_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.jokerhenchman_token,
        extra_conditions=[
            lambda: (can_beat_jht(state, options, player) and state.has(ItemName.jht_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_steamboat(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.steamboat_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.steamboat_token,
        extra_conditions=[
            lambda: (can_beat_jht(state, options, player) and state.has(ItemName.jht_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_glider(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.glider_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.glider_token,
        extra_conditions=[
            lambda: (can_beat_jht(state, options, player) and state.has(ItemName.jht_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_clown(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.clowngoon_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.clowngoon_token,
        extra_conditions=[
            lambda: (can_beat_lfabt(state, options, player) and state.has(ItemName.lfabt_lvl, player)) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_private_jet(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.privatejet_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.privatejet_token,
        extra_conditions=[
            lambda: state.has(ItemName.fotb_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_bruce_wayne(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.brucewayne_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.brucewayne_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_alfred(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.alfred_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.alfred_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_batgirl(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.batgirl_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.batgirl_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_nightwing(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.nightwing_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.nightwing_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_officer(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policeofficer_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policeofficer_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_military_police(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.militarypoliceman_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.militarypoliceman_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_security_guard(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.securityguard_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.securityguard_token,
        extra_conditions=[
            lambda: can_complete_any_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_bat_tank(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.battank_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.battank_token,
        extra_conditions=[
            lambda: can_complete_all_hero_episode(state, options, player) if
            options.decouple_character_tokens == 0 else True]
    )


def can_purchase_freeze_kart(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.freezekart_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.freezekart_token,
        extra_conditions=[
            lambda: state.has(ItemName.otr_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_iceberg(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.iceberg_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.iceberg_token,
        extra_conditions=[
            lambda: state.has(ItemName.otr_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_scientist(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.scientist_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.scientist_token,
        extra_conditions=[
            lambda: state.has(ItemName.aet_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_armoured_truck(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.armouredtruck_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.armouredtruck_token,
        extra_conditions=[
            lambda: state.has(ItemName.aet_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_swat(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.swat_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.swat_token,
        extra_conditions=[
            lambda: state.has(ItemName.bb_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_riddler_jet(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.riddlerjet_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.riddlerjet_token,
        extra_conditions=[
            lambda: state.has(ItemName.bb_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_sailor(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.sailor_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.sailor_token,
        extra_conditions=[
            lambda: state.has(ItemName.rtd_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_catwoman_classic(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.catwomanclassic_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.catwomanclassic_token,
        extra_conditions=[
            lambda: state.has(ItemName.sts_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_cat_motorcycle(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.catmotorcycle_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.catmotorcycle_token,
        extra_conditions=[
            lambda: state.has(ItemName.sts_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_watercraft(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policewatercraft_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policewatercraft_token,
        extra_conditions=[
            lambda: state.has(ItemName.hag_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_boat(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policeboat_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policeboat_token,
        extra_conditions=[
            lambda: state.has(ItemName.hag_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_commissioner(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.commissionergordon_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.commissionergordon_token,
        extra_conditions=[
            lambda: state.has(ItemName.asftc_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_hammer_truck(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.hammertruck_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.hammertruck_token,
        extra_conditions=[
            lambda: state.has(ItemName.asftc_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_heli(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policehelicopter_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policehelicopter_token,
        extra_conditions=[
            lambda: state.has(ItemName.bbpl_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_goon_heli(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.goonhelicopter_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.goonhelicopter_token,
        extra_conditions=[
            lambda: state.has(ItemName.bbpl_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_garbage_truck(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.garbagetruck_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.garbagetruck_token,
        extra_conditions=[
            lambda: state.has(ItemName.tlotn_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_police_marksman(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.policemarksman_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.policemarksman_token,
        extra_conditions=[
            lambda: state.has(ItemName.dol_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_joker_tropic(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.jokertropical_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.jokertropical_token,
        extra_conditions=[
            lambda: state.has(ItemName.dol_lvl, player) if options.decouple_character_tokens == 0 else True]
    )


def can_purchase_hush(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.hush_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.hush_token,
        extra_conditions=[
            lambda: state.has("UNIQUE_HOSTAGES", player, options.hush_purchase_requirements.value) if
            options.decouple_hush_and_ras_token.value == 0 else True],
    )


def can_purchase_ras(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(
        LocationName.rasalghul_unlocked,
        state,
        options,
        player,
        required_items=[],
        required_token=ItemName.rasalghul_token,
        extra_conditions=[
            lambda: state.has("UNIQUE_MINIKITS", player, options.ras_purchase_requirements.value) if
            options.decouple_hush_and_ras_token.value == 0 else True],
    )


def can_unlock_heat_suit(state: CollectionState, player: int):
    return can_beat_apa(state, player)


def can_unlock_glide_suit(state: CollectionState, options: LB1Options, player: int):
    return (
            True
            and ((state.has(ItemName.air_lvl, player) and can_beat_air(state, options, player))
                 or state.has(ItemName.tfo_lvl, player)
                 or (True)
                 or (state.has(ItemName.utc_lvl, player) and can_beat_utc(state, options, player))
                 or state.has(ItemName.pl_lvl, player)
                 or (True)
                 or (state.has(ItemName.tttot_lvl, player) and can_beat_tttot(state, options, player)))
    )


def can_unlock_demo_suit(state: CollectionState, options: LB1Options, player: int):
    return (
            True
            and (state.has(ItemName.ycbob_lvl, player)
                 or (state.has(ItemName.tsga_lvl, player) and can_beat_tsga(state, options, player))
                 or (True)
                 or (state.has(ItemName.zc_lvl, player) and can_beat_zc(state, options, player))
                 or state.has(ItemName.lfabt_lvl, player)
                 or state.has(ItemName.itdn_lvl, player)
                 or state.has(ItemName.tttot_lvl, player))
    )


def can_unlock_mag_suit(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and (state.has(ItemName.air_lvl, player)
                     or (True)
                     or state.has(ItemName.tsga_lvl, player)
                     or state.has(ItemName.utc_lvl, player)
                     or state.has(ItemName.zc_lvl, player)
                     or state.has(ItemName.jht_lvl, player) and can_beat_jht(state, options, player)
                     or (True
                         and True)
                     or state.has(ItemName.itdn_lvl, player) and can_beat_itdn(state, options, player)
                     or True)
        )
    else:
        return (
                True
                and (state.has(ItemName.air_lvl, player)
                     or (state.has(ItemName.tfo_lvl, player) and char_can_glide(state, player))
                     or state.has(ItemName.tsga_lvl, player)
                     or state.has(ItemName.utc_lvl, player)
                     or state.has(ItemName.zc_lvl, player)
                     or state.has(ItemName.jht_lvl, player) and can_beat_jht(state, options, player)
                     or (state.has(ItemName.lfabt_lvl, player) and char_can_explode(state, player)
                         and True)
                     or state.has(ItemName.itdn_lvl, player) and can_beat_itdn(state, options, player)
                     or state.has(ItemName.tttot_lvl, player) and char_can_explode(state, player))
        )


def can_unlock_sonic_suit(state: CollectionState, options: LB1Options, player: int):
    has_suit = True
    apa_path = state.has(ItemName.apa_lvl, player)

    if options.freeplay_or_story == 0:

        zc_path = (
                state.has(ItemName.zc_lvl, player)
                and True
                and True
                and True
        )
        lfabt_path = (
                state.has(ItemName.lfabt_lvl, player)
                and True
        )
        return has_suit and (apa_path or zc_path or lfabt_path)

    else:
        zc_path = (
                state.has(ItemName.zc_lvl, player)
                and (
                        (True and char_can_glide(state, player))
                        or char_can_explode(state, player)
                )
        )
        lfabt_path = (
                state.has(ItemName.lfabt_lvl, player)
                and char_can_explode(state, player)
        )
        return has_suit and (apa_path or zc_path or lfabt_path)


def can_unlock_water_suit(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and ((True
                      and True)
                     or True)
        )
    else:
        return (
                True
                and ((state.has(ItemName.utc_lvl, player)
                      and (True and True)
                      or char_can_explode(state, player))
                     or state.has(ItemName.zc_lvl, player) and char_can_glide(state, player))
        )


def can_unlock_tech_suit(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and (((True)
                      or (state.has(ItemName.tsga_lvl, player)
                          and True and True)
                      or (state.has(ItemName.zc_lvl, player)
                          and True and True)
                      or (True)))
        )
    else:
        return (
                True
                and ((state.has(ItemName.ycbob_lvl, player) and char_can_explode(state, player))
                     or (state.has(ItemName.tsga_lvl, player)
                         and True and char_can_glide(state, player))
                     or (state.has(ItemName.zc_lvl, player)
                         and (True and char_can_glide(state, player)
                              or char_can_explode(state, player))
                         or (state.has(ItemName.itdn_lvl, player) and char_can_explode(state, player))))
        )


def can_unlock_attract_suit(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and ((True)
                     or (state.has(ItemName.tfo_lvl, player)
                         and True and True)
                     or (state.has(ItemName.jht_lvl, player))
                     or (True
                         and True and True))
        )
    else:
        return (
                True
                and ((True)
                     or (state.has(ItemName.tfo_lvl, player)
                         and True and char_can_glide(state, player))
                     or (state.has(ItemName.jht_lvl, player))
                     or (state.has(ItemName.lfabt_lvl, player) and char_can_explode(state, player)
                         and True and True))
        )


def can_beat_ycbob(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_air(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                True
                and char_can_glide(state, player)
        )


def can_beat_apa(state: CollectionState, player: int):
    return (
            True
            and True
            and True
    )


def can_beat_tfo(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                True
                and (True or char_can_cross_toxic(state, player))
        )


def can_beat_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
                and True
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
                and True
                and char_can_glide(state, player)
        )


def can_beat_utc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                # and True
                and char_can_sink(state, player)
                and char_can_explode(state, player)
        )


def can_beat_zc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
                and True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                and True
                and char_can_explode(state, player)
                and True
        )


def can_beat_pl(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_sink(state, player)
        )


def can_beat_jht(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                and True
                and True
        )


def can_beat_lfabt(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
                and True
        )
    else:
        return (
                char_can_explode(state, player)
                and True
                and True
        )


def can_beat_itdn(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
        )
    else:
        return (
                True
                and char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_beat_tttot(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
                and True
        )
    else:
        return (
                True
                and char_can_glide(state, player)
        )


# Whole level locked by glide
def level_access_tfo(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
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
                True
                and True
                and state.has(ItemName.jht_lvl, player)
        )
    else:
        return (
                char_can_glide(state, player)
                and True
                and state.has(ItemName.jht_lvl, player)
        )


# Free Access functions are needed for moving about in freeplay (moves story characters have)
def free_access_ycbob(state: CollectionState, player: int):
    return char_can_explode(state, player)


def free_access_air(state: CollectionState, player: int):
    return (
            True
            and char_can_glide(state, player)
    )


def free_access_tfc(state: CollectionState, player: int):
    return auto_has_cable(state, player)


def free_access_apa(state: CollectionState, player: int):
    return (
            True
            and True
    )


def free_access_tfo(state: CollectionState, player: int):
    return True


def free_access_tsga(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                and True
        )


def free_access_bbb(state: CollectionState, player: int):
    return state.has(ItemName.batboat_unlocked, player)


def free_access_utc(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_sink(state, player)
            and (True or char_can_glide(state, player))
    )


def free_access_zc(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    return (
            char_can_explode(state, player)
            or (True and char_can_glide(state, player))
    )


def free_access_pl(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                and char_can_sink(state, player)
        )


def free_access_lfabt(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return True and True
    else:
        return char_can_explode(state, player) and True


def free_access_itdn(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return True
    else:
        return char_can_explode(state, player)


def free_access_tttot(state: CollectionState, player: int):
    return True


def free_access_trmaw(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and char_is_strong(state, player)
    )


def free_access_otr(state: CollectionState, player: int):
    return state.has(ItemName.mrfreeze_unlocked, player)


def free_access_gf(state: CollectionState, player: int):
    return char_can_hypno(state, player) and state.has(ItemName.poisonivy_unlocked, player)


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
            and state.has(ItemName.scarecrowbiplane_unlocked, player)
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
                and True
        )
    else:
        return True


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
                and True
                and True
        )
    else:
        return (
                True
                and True
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
        return True
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
                True
                and True
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
                and True
        )


def can_apa_min5(state: CollectionState, player: int):
    return True


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
                and True
                and char_can_explode(state, player)
        )
    else:
        return (
                True
                and char_can_explode(state, player)
        )


def can_apa_min8(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_apa(state, player)
                and True
                and char_can_double_jump(state, player)
        )
    else:
        return (
                True
                and char_can_double_jump(state, player)
        )


def can_apa_min9(state: CollectionState, player: int):
    return True


def can_apa_min10(state: CollectionState, player: int):
    return True


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
        )
    else:
        return (
                char_can_double_jump(state, player)
                and True
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
        return True
    else:
        return True or char_can_cross_toxic(state, player)


def can_tfo_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return True
    else:
        return True or char_can_cross_toxic(state, player)


def can_tsga_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tsga(state, options, player)
                and True
                and char_can_access_female_room(state, player)
        )
    else:
        return (
                True
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
            and True
    )


def can_tsga_min10(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tsga(state, options, player)
            and char_can_sink(state, player)
            and True
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
                and True
                and char_is_strong(state, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_sink(state, player)
                and char_is_strong(state, player)
                and True
        )


def can_utc_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_utc(state, options, player)
                and char_can_double_jump(state, player)
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
                and True
        )
    else:
        return True


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
    if options.freeplay_or_story == 0:
        return can_beat_utc(state, options, player)
    else:
        return True


def can_utc_min9(state: CollectionState, options: LB1Options, player: int):
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
                and True
                and (char_can_access_female_room(state, player)
                     or (char_can_cross_toxic(state, player) and char_is_strong(state, player)))
        )
    else:
        return (
                True
                and (char_can_access_female_room(state, player)
                     or (char_can_cross_toxic(state, player) and char_is_strong(state, player)))
        )


def can_zc_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and char_can_double_jump(state, player)
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
                True
                and True
        )
    else:
        return (
                char_can_glide(state, player)
                and True
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
                and True
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
                and True
                and char_is_strong(state, player)
        )


def can_pl_min1(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_zc(state, options, player)
                and True
        )
    else:
        return True


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


def can_pl_min5(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                True
                and char_can_sink(state, player)
        )


def can_pl_min7(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_pl_min8(state: CollectionState, player: int):
    return (
            char_can_cross_toxic(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_pl_min10(state: CollectionState, player: int):
    return (
            True
            and True
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
                and True
        )
    else:
        return (
                char_can_hypno(state, player)
                and char_can_explode(state, player)
                and True
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
        )
    else:
        return (
                char_joker(state, player)
                and True
        )


def can_jht_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and char_can_explode(state, player)
        )
    else:
        return (
                char_can_explode(state, player)
                and True
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
        )
    else:
        return (
                char_can_long_jump(state, player)
                and True
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
        return True
    else:
        return char_can_explode(state, player)


def can_lfabt_min6(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_lfabt(state, options, player)
                and char_joker(state, player)
        )
    else:
        return (
                char_joker(state, player)
                and True
        )


def can_lfabt_min7(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return can_beat_lfabt(state, options, player)
    else:
        return (
                True
                and True
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
                True
                and True
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
                True
                and True
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
                True
                and True
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
                and True
        )
    else:
        return (
                char_is_strong(state, player)
                and True
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
                and True
        )
    else:
        return (
                True
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
            and True
    )


def can_itdn_min10(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_itdn(state, options, player)
                and char_joker(state, player)
                and True
                and char_can_double_jump(state, player)
        )
    else:
        return (
                char_joker(state, player)
                and True
                and char_can_double_jump(state, player)
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
                and True
        )
    else:
        return True


def can_tttot_min4(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tttot(state, options, player)
                and True
        )
    else:
        return True


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
            (char_can_explode(state, player) and True)
            or (char_can_double_jump(state, player) and True)
    )


def can_otr_min2(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and char_can_hypno(state, player)
            and True
    )


def can_otr_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_otr_min5(state: CollectionState, player: int):
    return True


def can_otr_min7(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and True
    )


def can_otr_min8(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and char_can_explode(state, player)
    )


def can_otr_min9(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and True
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
    return char_can_explode(state, player)


def can_gf_min5(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and True
    )


def can_gf_min6(state: CollectionState, player: int):
    return (
            True
            and True
    )


def can_gf_min7(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_is_strong(state, player)
            and True
    )


def can_gf_min8(state: CollectionState, player: int):
    return True


def can_gf_min9(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and True
    )


def can_gf_min10(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_aet_min1(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and True
    )


def can_aet_min2(state: CollectionState, player: int):
    return (
            char_can_techno(state, player)
            and True
    )


def can_aet_min3(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_aet_min4(state: CollectionState, player: int):
    return True


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
            True
            and char_can_cross_toxic(state, player)
    )


def can_aet_min9(state: CollectionState, player: int):
    return (
            True
            and char_can_cross_toxic(state, player)
    )


def can_bb_min2(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_bb_min4(state: CollectionState, player: int):
    return (
            True
            and True
            and True
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
            True
            and True
            and char_can_cross_toxic(state, player)
    )


def can_bb_min10(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and char_can_cross_toxic(state, player)
    )


def can_rtd_min1(state: CollectionState, player: int):
    return (
            True
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
            and True
            and char_can_cross_toxic(state, player)
    )


def can_sts_min1(state: CollectionState, player: int):
    return (
            char_is_strong(state, player)
            and True
    )


def can_sts_min3(state: CollectionState, player: int):
    return (
            char_can_glide(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_sts_min6(state: CollectionState, player: int):
    return True


def can_sts_min7(state: CollectionState, player: int):
    return (
            True
            and char_is_strong(state, player)
    )


def can_sts_min9(state: CollectionState, player: int):
    return (
            True
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
    return True


def can_adr_min5(state: CollectionState, player: int):
    return (
            True
            and state.has(ItemName.penguin_unlocked, player)
            and (True or char_can_hypno(state, player))
    )


def can_adr_min6(state: CollectionState, player: int):
    return (
            char_can_hypno(state, player)
            and state.has(ItemName.mrfreeze_unlocked, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_adr_min7(state: CollectionState, player: int):
    return True


def can_adr_min9(state: CollectionState, player: int):
    return (
            True
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_aw_min1(state: CollectionState, player: int):
    return char_can_sink(state, player)


def can_aw_min2(state: CollectionState, player: int):
    return (
            True
            and True
            and char_joker(state, player)
            and char_is_strong(state, player)
            and char_can_double_jump(state, player)
    )


def can_aw_min3(state: CollectionState, player: int):
    return (
            True
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
    return True


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
    return True


def can_asftc_min3(state: CollectionState, player: int):
    return (
            state.has(ItemName.mrfreeze_unlocked, player)
            and char_joker(state, player)
    )


def can_asftc_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_asftc_min5(state: CollectionState, player: int):
    return True


def can_asftc_min7(state: CollectionState, player: int):
    return (
            True
            and char_can_explode(state, player)
    )


def can_asftc_min8(state: CollectionState, player: int):
    return (
            char_can_sink(state, player)
            and char_joker(state, player)
    )


def can_asftc_min9(state: CollectionState, player: int):
    return (
            True
            and char_joker(state, player)
            and char_can_techno(state, player)
    )


def can_bbpl_min3(state: CollectionState, player: int):
    return state.has(ItemName.batwing_unlocked, player)


def can_tjm_min3(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_tjm_min4(state: CollectionState, player: int):
    return True


def can_tjm_min5(state: CollectionState, player: int):
    return True


def can_tjm_min6(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_tjm_min7(state: CollectionState, player: int):
    return (
            True
            and char_can_explode(state, player)
            and True
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
            True
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
            and True
            and (char_can_glide(state, player) or char_can_double_jump(state, player))
    )


def can_dol_min1(state: CollectionState, player: int):
    return state.has(ItemName.poisonivy_unlocked, player)


def can_dol_min2(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and True
    )


def can_dol_min3(state: CollectionState, player: int):
    return char_is_strong(state, player)


def can_dol_min4(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_dol_min5(state: CollectionState, player: int):
    return True


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
    return True


def can_tfo_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_tfo(state, options, player)
                and char_can_double_jump(state, player)
        )
    else:
        return (
                True
                and char_can_double_jump(state, player)
        )


def can_utc_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return char_can_explode(state, player)


def can_zc_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return True
    else:
        return (
                True
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
                True
                and True
        )
    else:
        return True


def can_itdn_host(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                True
                and True
        )
    else:
        return (
                char_can_explode(state, player)
                and char_can_techno(state, player)
        )


def can_trmaw_host(state: CollectionState, player: int):
    return True


def can_otr_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_gf_host(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and state.has(ItemName.poisonivy_unlocked, player)
    )


def can_aet_host(state: CollectionState, player: int):
    return True


def can_bb_host(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_rtd_host(state: CollectionState, player: int):
    return True


def can_sts_host(state: CollectionState, player: int):
    return (
            True
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
            and True
    )


def can_tlotn_host(state: CollectionState, player: int):
    return char_can_double_jump(state, player)


def can_dol_host(state: CollectionState, player: int):
    return char_can_glide(state, player)


def can_ycbob_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return True and True
    else:
        return char_can_techno(state, player) and char_can_explode(state, player)


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
                and True
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
            and True
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
    return True


def can_jht_rb(state: CollectionState, options: LB1Options, player: int):
    if options.freeplay_or_story == 0:
        return (
                can_beat_jht(state, options, player)
                and state.has(ItemName.mrfreeze_unlocked, player)
                and True
                and char_can_double_jump(state, player)
        )
    else:
        return (
                state.has(ItemName.mrfreeze_unlocked, player)
                and True
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
            and True
    )


def can_tttot_rb(state: CollectionState, options: LB1Options, player: int):
    return (
            can_beat_tttot(state, options, player)
            and char_is_strong(state, player)
    )


def can_trmaw_rb(state: CollectionState, player: int):
    return (
            char_can_double_jump(state, player)
            and True
    )


def can_otr_rb(state: CollectionState, player: int):
    return char_can_explode(state, player)


def can_gf_rb(state: CollectionState, player: int):
    return (
            char_can_explode(state, player)
            and True
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
            and True
    )


def can_rtd_rb(state: CollectionState, player: int):
    return (
            char_can_access_female_room(state, player)
            and char_is_strong(state, player)
            and state.has(ItemName.penguin_unlocked, player)
    )


def can_sts_rb(state: CollectionState, player: int):
    return (
            True
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
            and True
    )


def can_aw_rb(state: CollectionState, player: int):
    return char_can_cross_toxic(state, player) and True


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
            and True
    )


def can_tlotn_rb(state: CollectionState, player: int):
    return (
            state.has(ItemName.poisonivy_unlocked, player)
            and char_can_double_jump(state, player)
            and True
    )


def can_purchase_silhouettes(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.silhouettes, state, options, player)


def can_purchase_beepbeep(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.beepbeep, state, options, player)


def can_purchase_ice_rink(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.icerink, state, options, player)


def can_purchase_disguise(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.disguise, state, options, player)


def can_purchase_extra_toggle(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.extratoggle, state, options, player)


def can_purchase_scorex2(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.scorex2, state, options, player, required_items=[ItemName.trmaw_rbc])


def can_purchase_scorex4(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.scorex4, state, options, player, required_items=[ItemName.otr_rbc])


def can_purchase_scorex6(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.scorex6, state, options, player, required_items=[ItemName.gf_rbc])


def can_purchase_scorex8(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.scorex8, state, options, player, required_items=[ItemName.aet_rbc])


def can_purchase_scorex10(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.scorex10, state, options, player, required_items=[ItemName.bb_rbc])


def can_purchase_stud_magnet(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.studmagnet, state, options, player, required_items=[ItemName.rtd_rbc])


def can_purchase_char_studs(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.charstuds, state, options, player, required_items=[ItemName.sts_rbc])


def can_purchase_minikit_detect(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.minikitdetect, state, options, player, required_items=[ItemName.hag_rbc])


def can_purchase_powerbrick_detect(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.pwrbrickdetect, state, options, player,
                                  required_items=[ItemName.adr_rbc])


def can_purchase_always_score(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.alwaysscore, state, options, player, required_items=[ItemName.aw_rbc])


def can_purchase_fast_build(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.fastbuild, state, options, player, [ItemName.asftc_rbc])


def can_purchase_immune_freeze(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.immunefreeze, state, options, player, required_items=[ItemName.bbpl_rbc])


def can_purchase_regen_hearts(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.regenhearts, state, options, player, required_items=[ItemName.tjm_rbc])


def can_purchase_extra_hearts(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.extrahearts, state, options, player, required_items=[ItemName.tlotn_rbc])


def can_purchase_invincibility(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.invincibility, state, options, player, required_items=[ItemName.dol_rbc])


def can_purchase_fast_grapple(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.fastgrapple, state, options, player, required_items=[ItemName.ycbob_rbc])


def can_purchase_fast_batarang(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.fastbatarang, state, options, player, required_items=[ItemName.air_rbc])


def can_purchase_more_targets(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.moretargets, state, options, player, required_items=[ItemName.tfc_rbc])


def can_purchase_flaming_bat(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.flamingbata, state, options, player, required_items=[ItemName.apa_rbc])


def can_purchase_slam(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.slam, state, options, player, required_items=[ItemName.tfo_rbc])


def can_purchase_more_det(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.moredet, state, options, player, required_items=[ItemName.tsga_rbc])


def can_purchase_armor_plating(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.armorplating, state, options, player, required_items=[ItemName.bbb_rbc])


def can_purchase_sonic_pain(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.sonicpain, state, options, player, required_items=[ItemName.utc_rbc])


def can_purchase_area_effect(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.areaeffect, state, options, player, required_items=[ItemName.zc_rbc])


def can_purchase_bats(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.bats, state, options, player, required_items=[ItemName.pl_rbc])


def can_purchase_freeze_bat(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.freezebatarang, state, options, player,
                                  required_items=[ItemName.jht_rbc])


def can_purchase_decoy(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.decoy, state, options, player, required_items=[ItemName.lfabt_rbc])


def can_purchase_fast_walk(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.fastwalk, state, options, player, required_items=[ItemName.fotb_rbc])


def can_purchase_faster_pieces(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.fasterpieces, state, options, player, required_items=[ItemName.itdn_rbc])


def can_purchase_piece_detect(state: CollectionState, options: LB1Options, player: int):
    return can_purchase_shop_item(LocationName.piecedetect, state, options, player, required_items=[ItemName.tttot_rbc])


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


def set_char_rules(world: MultiWorld, options: LB1Options, player: int):
    # set_rule(world.get_location(LocationName.batman_collected, player),
    #          lambda state: can_complete_any_hero_level(state, options, player))
    # set_rule(world.get_location(LocationName.robin_collected, player),
    #          lambda state: can_complete_any_hero_level(state, options, player))
    # Batmobile, Cycle, Boat, Sub, Wing, Copter don't require anything to beat level
    set_rule(world.get_location(LocationName.twoface_unlocked, player),
             lambda state: can_unlock_two_face(state, player))
    set_rule(world.get_location(LocationName.riddler_unlocked, player),
             lambda state: can_unlock_riddler(state, player))
    set_rule(world.get_location(LocationName.catwoman_unlocked, player),
             lambda state: can_unlock_catwoman(state, player))
    set_rule(world.get_location(LocationName.penguin_unlocked, player),
             lambda state: can_unlock_penguin(state, player))
    set_rule(world.get_location(LocationName.harleyquinn_unlocked, player),
             lambda state: can_unlock_harley(state, player))
    set_rule(world.get_location(LocationName.joker_unlocked, player),
             lambda state: can_unlock_joker(state, player))
    # Villain levels can be beaten in story


def set_suit_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_location(LocationName.heatprotectsuit, player),
             lambda state: can_unlock_heat_suit(state, player))
    set_rule(world.get_location(LocationName.glidesuit, player),
             lambda state: can_unlock_glide_suit(state, options, player))
    set_rule(world.get_location(LocationName.demosuit, player),
             lambda state: can_unlock_demo_suit(state, options, player))
    set_rule(world.get_location(LocationName.sonicsuit, player),
             lambda state: can_unlock_sonic_suit(state, options, player))
    set_rule(world.get_location(LocationName.watersuit, player),
             lambda state: can_unlock_water_suit(state, options, player))
    set_rule(world.get_location(LocationName.techsuit, player),
             lambda state: can_unlock_tech_suit(state, options, player))
    set_rule(world.get_location(LocationName.magsuit, player),
             lambda state: can_unlock_mag_suit(state, options, player))
    set_rule(world.get_location(LocationName.attractsuit, player),
             lambda state: can_unlock_attract_suit(state, options, player))


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
    set_rule(world.get_location(LocationName.pl_min5, player), lambda state: can_pl_min5(state, options, player))
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
    # set_rule(world.get_location(LocationName.aw_min8, player), lambda state: can_aw_min8(state, player))
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
    # BBPL Minikits can be done in story or with freeplay region access except min 3
    set_rule(world.get_location(LocationName.bbpl_min3, player), lambda state: can_bbpl_min3(state, player))
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


def set_shop_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_location(LocationName.riddlergoon_unlocked, player),
             lambda state: can_purchase_riddler_goon(state, options, player))
    set_rule(world.get_location(LocationName.riddlerhenchman_unlocked, player),
             lambda state: can_purchase_riddler_henchman(state, options, player))
    set_rule(world.get_location(LocationName.freezegirl_unlocked, player),
             lambda state: can_purchase_freeze_girl(state, options, player))
    set_rule(world.get_location(LocationName.policecar_unlocked, player),
             lambda state: can_purchase_police_car(state, options, player))
    set_rule(world.get_location(LocationName.policebike_unlocked, player),
             lambda state: can_purchase_police_bike(state, options, player))
    set_rule(world.get_location(LocationName.policevan_unlocked, player),
             lambda state: can_purchase_police_van(state, options, player))
    set_rule(world.get_location(LocationName.jokervan_unlocked, player),
             lambda state: can_purchase_joker_van(state, options, player))
    set_rule(world.get_location(LocationName.poisonivygoon_unlocked, player),
             lambda state: can_purchase_poison_ivy_goon(state, options, player))
    set_rule(world.get_location(LocationName.fishmonger_unlocked, player),
             lambda state: can_purchase_fishmonger(state, options, player))
    set_rule(world.get_location(LocationName.penguingoon_unlocked, player),
             lambda state: can_purchase_penguin_goon(state, options, player))
    set_rule(world.get_location(LocationName.penguinhenchman_unlocked, player),
             lambda state: can_purchase_penguin_henchman(state, options, player))
    set_rule(world.get_location(LocationName.robinssubmarine_unlocked, player),
             lambda state: can_purchase_robin_sub(state, options, player))
    set_rule(world.get_location(LocationName.penguingoonsub_unlocked, player),
             lambda state: can_purchase_goon_sub(state, options, player))
    set_rule(world.get_location(LocationName.harbourhelicopter_unlocked, player),
             lambda state: can_purchase_harbour_heli(state, options, player))
    set_rule(world.get_location(LocationName.zoosweeper_unlocked, player),
             lambda state: can_purchase_zoo_sweeper(state, options, player))
    set_rule(world.get_location(LocationName.manbat_unlocked, player),
             lambda state: can_purchase_manbat(state, options, player))
    set_rule(world.get_location(LocationName.yeti_unlocked, player),
             lambda state: can_purchase_yeti(state, options, player))
    set_rule(world.get_location(LocationName.penguinminion_unlocked, player),
             lambda state: can_purchase_penguin_minion(state, options, player))
    set_rule(world.get_location(LocationName.madhatter_unlocked, player),
             lambda state: can_purchase_mad_hatter(state, options, player))
    set_rule(world.get_location(LocationName.jokergoon_unlocked, player),
             lambda state: can_purchase_joker_goon(state, options, player))
    set_rule(world.get_location(LocationName.jokerhenchman_unlocked, player),
             lambda state: can_purchase_joker_henchman(state, options, player))
    set_rule(world.get_location(LocationName.steamboat_unlocked, player),
             lambda state: can_purchase_steamboat(state, options, player))
    set_rule(world.get_location(LocationName.glider_unlocked, player),
             lambda state: can_purchase_glider(state, options, player))
    set_rule(world.get_location(LocationName.clowngoon_unlocked, player),
             lambda state: can_purchase_clown(state, options, player))
    set_rule(world.get_location(LocationName.privatejet_unlocked, player),
             lambda state: can_purchase_private_jet(state, options, player))
    set_rule(world.get_location(LocationName.brucewayne_unlocked, player),
             lambda state: can_purchase_bruce_wayne(state, options, player))
    set_rule(world.get_location(LocationName.alfred_unlocked, player),
             lambda state: can_purchase_alfred(state, options, player))
    set_rule(world.get_location(LocationName.batgirl_unlocked, player),
             lambda state: can_purchase_batgirl(state, options, player))
    set_rule(world.get_location(LocationName.nightwing_unlocked, player),
             lambda state: can_purchase_nightwing(state, options, player))
    set_rule(world.get_location(LocationName.policeofficer_unlocked, player),
             lambda state: can_purchase_police_officer(state, options, player))
    set_rule(world.get_location(LocationName.militarypoliceman_unlocked, player),
             lambda state: can_purchase_military_police(state, options, player))
    set_rule(world.get_location(LocationName.securityguard_unlocked, player),
             lambda state: can_purchase_security_guard(state, options, player))
    set_rule(world.get_location(LocationName.battank_unlocked, player),
             lambda state: can_purchase_bat_tank(state, options, player))
    set_rule(world.get_location(LocationName.freezekart_unlocked, player),
             lambda state: can_purchase_freeze_kart(state, options, player))
    set_rule(world.get_location(LocationName.iceberg_unlocked, player),
             lambda state: can_purchase_iceberg(state, options, player))
    set_rule(world.get_location(LocationName.scientist_unlocked, player),
             lambda state: can_purchase_scientist(state, options, player))
    set_rule(world.get_location(LocationName.armouredtruck_unlocked, player),
             lambda state: can_purchase_armoured_truck(state, options, player))
    set_rule(world.get_location(LocationName.swat_unlocked, player),
             lambda state: can_purchase_swat(state, options, player))
    set_rule(world.get_location(LocationName.riddlerjet_unlocked, player),
             lambda state: can_purchase_riddler_jet(state, options, player))
    set_rule(world.get_location(LocationName.sailor_unlocked, player),
             lambda state: can_purchase_sailor(state, options, player))
    set_rule(world.get_location(LocationName.catwomanclassic_unlocked, player),
             lambda state: can_purchase_catwoman_classic(state, options, player))
    set_rule(world.get_location(LocationName.catmotorcycle_unlocked, player),
             lambda state: can_purchase_cat_motorcycle(state, options, player))
    set_rule(world.get_location(LocationName.policewatercraft_unlocked, player),
             lambda state: can_purchase_police_watercraft(state, options, player))
    set_rule(world.get_location(LocationName.policeboat_unlocked, player),
             lambda state: can_purchase_police_boat(state, options, player))
    set_rule(world.get_location(LocationName.commissionergordon_unlocked, player),
             lambda state: can_purchase_commissioner(state, options, player))
    set_rule(world.get_location(LocationName.hammertruck_unlocked, player),
             lambda state: can_purchase_hammer_truck(state, options, player))
    set_rule(world.get_location(LocationName.policehelicopter_unlocked, player),
             lambda state: can_purchase_police_heli(state, options, player))
    set_rule(world.get_location(LocationName.goonhelicopter_unlocked, player),
             lambda state: can_purchase_goon_heli(state, options, player))
    set_rule(world.get_location(LocationName.garbagetruck_unlocked, player),
             lambda state: can_purchase_garbage_truck(state, options, player))
    set_rule(world.get_location(LocationName.policemarksman_unlocked, player),
             lambda state: can_purchase_police_marksman(state, options, player))
    set_rule(world.get_location(LocationName.jokertropical_unlocked, player),
             lambda state: can_purchase_joker_tropic(state, options, player))
    set_rule(world.get_location(LocationName.hush_unlocked, player),
             lambda state: can_purchase_hush(state, options, player))
    set_rule(world.get_location(LocationName.rasalghul_unlocked, player),
             lambda state: can_purchase_ras(state, options, player))

    set_rule(world.get_location(LocationName.silhouettes, player),
             lambda state: can_purchase_silhouettes(state, options, player))
    set_rule(world.get_location(LocationName.beepbeep, player),
             lambda state: can_purchase_beepbeep(state, options, player))
    set_rule(world.get_location(LocationName.icerink, player),
             lambda state: can_purchase_ice_rink(state, options, player))
    set_rule(world.get_location(LocationName.disguise, player),
             lambda state: can_purchase_disguise(state, options, player))
    set_rule(world.get_location(LocationName.extratoggle, player),
             lambda state: can_purchase_extra_toggle(state, options, player))
    set_rule(world.get_location(LocationName.scorex2, player),
             lambda state: can_purchase_scorex2(state, options, player))
    set_rule(world.get_location(LocationName.scorex4, player),
             lambda state: can_purchase_scorex4(state, options, player))
    set_rule(world.get_location(LocationName.scorex6, player),
             lambda state: can_purchase_scorex6(state, options, player))
    set_rule(world.get_location(LocationName.scorex8, player),
             lambda state: can_purchase_scorex8(state, options, player))
    set_rule(world.get_location(LocationName.scorex10, player),
             lambda state: can_purchase_scorex10(state, options, player))
    set_rule(world.get_location(LocationName.studmagnet, player),
             lambda state: can_purchase_stud_magnet(state, options, player))
    set_rule(world.get_location(LocationName.charstuds, player),
             lambda state: can_purchase_char_studs(state, options, player))
    set_rule(world.get_location(LocationName.minikitdetect, player),
             lambda state: can_purchase_minikit_detect(state, options, player))
    set_rule(world.get_location(LocationName.pwrbrickdetect, player),
             lambda state: can_purchase_powerbrick_detect(state, options, player))
    set_rule(world.get_location(LocationName.alwaysscore, player),
             lambda state: can_purchase_always_score(state, options, player))
    set_rule(world.get_location(LocationName.fastbuild, player),
             lambda state: can_purchase_fast_build(state, options, player))
    set_rule(world.get_location(LocationName.immunefreeze, player),
             lambda state: can_purchase_immune_freeze(state, options, player))
    set_rule(world.get_location(LocationName.regenhearts, player),
             lambda state: can_purchase_regen_hearts(state, options, player))
    set_rule(world.get_location(LocationName.extrahearts, player),
             lambda state: can_purchase_extra_hearts(state, options, player))
    set_rule(world.get_location(LocationName.invincibility, player),
             lambda state: can_purchase_invincibility(state, options, player))
    set_rule(world.get_location(LocationName.fastgrapple, player),
             lambda state: can_purchase_fast_grapple(state, options, player))
    set_rule(world.get_location(LocationName.fastbatarang, player),
             lambda state: can_purchase_fast_batarang(state, options, player))
    set_rule(world.get_location(LocationName.moretargets, player),
             lambda state: can_purchase_more_targets(state, options, player))
    set_rule(world.get_location(LocationName.flamingbata, player),
             lambda state: can_purchase_flaming_bat(state, options, player))
    set_rule(world.get_location(LocationName.slam, player),
             lambda state: can_purchase_slam(state, options, player))
    set_rule(world.get_location(LocationName.moredet, player),
             lambda state: can_purchase_more_det(state, options, player))
    set_rule(world.get_location(LocationName.armorplating, player),
             lambda state: can_purchase_armor_plating(state, options, player))
    set_rule(world.get_location(LocationName.sonicpain, player),
             lambda state: can_purchase_sonic_pain(state, options, player))
    set_rule(world.get_location(LocationName.areaeffect, player),
             lambda state: can_purchase_area_effect(state, options, player))
    set_rule(world.get_location(LocationName.bats, player),
             lambda state: can_purchase_bats(state, options, player))
    set_rule(world.get_location(LocationName.freezebatarang, player),
             lambda state: can_purchase_freeze_bat(state, options, player))
    set_rule(world.get_location(LocationName.decoy, player),
             lambda state: can_purchase_decoy(state, options, player))
    set_rule(world.get_location(LocationName.fastwalk, player),
             lambda state: can_purchase_fast_walk(state, options, player))
    set_rule(world.get_location(LocationName.fasterpieces, player),
             lambda state: can_purchase_faster_pieces(state, options, player))
    set_rule(world.get_location(LocationName.piecedetect, player),
             lambda state: can_purchase_piece_detect(state, options, player))


def set_token_rules(world: MultiWorld, options: LB1Options, player: int):
    set_rule(world.get_location(LocationName.riddlergoon_collected, player),
             lambda state: can_beat_ycbob(state, options, player))
    set_rule(world.get_location(LocationName.riddlerhenchman_collected, player),
             lambda state: can_beat_ycbob(state, options, player))
    set_rule(world.get_location(LocationName.freezegirl_collected, player),
             lambda state: can_beat_air(state, options, player))
    # TFC can be completed in story - police car, bike, van, joker van don't require anything besides region logic
    set_rule(world.get_location(LocationName.poisonivygoon_collected, player),
             lambda state: can_beat_apa(state, player))
    set_rule(world.get_location(LocationName.fishmonger_collected, player),
             lambda state: can_beat_tsga(state, options, player))
    set_rule(world.get_location(LocationName.penguingoon_collected, player),
             lambda state: can_beat_tsga(state, options, player))
    set_rule(world.get_location(LocationName.penguinhenchman_collected, player),
             lambda state: can_beat_tsga(state, options, player))
    # BBB can be completed in story - robin sub, penguin goon sub, harbour helicopter don't require anything besides
    # region logic
    set_rule(world.get_location(LocationName.zoosweeper_collected, player),
             lambda state: can_beat_zc(state, options, player))
    set_rule(world.get_location(LocationName.manbat_collected, player),
             lambda state: can_beat_pl(state, options, player))
    set_rule(world.get_location(LocationName.yeti_collected, player),
             lambda state: can_beat_pl(state, options, player))
    set_rule(world.get_location(LocationName.penguinminion_collected, player),
             lambda state: can_beat_pl(state, options, player))
    set_rule(world.get_location(LocationName.madhatter_collected, player),
             lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.jokergoon_collected, player),
             lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.jokerhenchman_collected, player),
             lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.steamboat_collected, player),
             lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.glider_collected, player),
             lambda state: can_beat_jht(state, options, player))
    set_rule(world.get_location(LocationName.clowngoon_collected, player),
             lambda state: can_beat_lfabt(state, options, player))
    # FOTB can be completed in story - private jet doesn't require anything besides region logic
    set_rule(world.get_location(LocationName.brucewayne_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.alfred_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.batgirl_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.nightwing_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.policeofficer_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.militarypoliceman_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.securityguard_collected, player),
             lambda state: can_complete_any_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.battank_collected, player),
             lambda state: can_complete_all_hero_episode(state, options, player))
    set_rule(world.get_location(LocationName.hush_collected, player),
             lambda state: state.has("UNIQUE_HOSTAGES", player, options.hush_purchase_requirements.value))
    set_rule(world.get_location(LocationName.rasalghul_collected, player),
             lambda state: state.has("UNIQUE_MINIKITS", player, options.ras_purchase_requirements.value))
    # All villain levels can be completed in story - no additional logic needed besides region


def set_rules(world: MultiWorld, options: LB1Options, player: int):
    set_entrance_rules(world, options, player)
    set_char_rules(world, options, player)
    # Hard char Rules
    # set_suit_rules(world, options, player)
    if options.minikit_sanity == 1:
        set_minikit_rules(world, options, player)
    set_host_rules(world, options, player)
    set_level_beaten_rules(world, options, player)
    if options.true_status_sanity == 1:
        set_true_status_rules(world, options, player)
    set_red_brick_location_rules(world, options, player)
    set_shop_rules(world, options, player)
    if options.decouple_character_tokens == 1:
        set_token_rules(world, options, player)

    # Set End Goal
    if options.EndGoal == EndGoal.option_minikits:
        world.completion_condition[player] = lambda state: state.has("UNIQUE_MINIKITS", player, options.minikits_to_win)
    elif options.EndGoal == EndGoal.option_levels_beaten:
        world.completion_condition[player] = \
            lambda state: state.has("Level Beaten Token", player, options.levels_to_win)


def set_event_rules(world: MultiWorld, player: int):
    for (name, data) in event_location_table.items():
        event: Location = world.get_location(name, player)
        level_beaten_name = name.removesuffix(" Event")
        set_rule(event, world.get_location(level_beaten_name, player).access_rule)
