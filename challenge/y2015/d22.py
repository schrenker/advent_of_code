import itertools
import sys

# No meaningful tests provided by AoC
test_results = {"part_one": {}, "part_two": {}}


class game:
    def __init__(self, input, spell_list, hard_mode):
        self.mana = 500
        self.hp = 50
        self.boss_hp, self.boss_dmg = tuple(
            int(x.split()[-1]) for x in input.splitlines()
        )

        self.poison_status = 0
        self.shield_status = 0
        self.recharge_status = 0

        self.poison_damage = 3
        self.shield_armor = 7
        self.recharge_amount = 101

        self.spell_list = spell_list
        self.hard_mode = hard_mode
        self.mana_spent = 0

    def missile(self):
        self.mana -= 53
        self.mana_spent += 53
        return 4

    def drain(self):
        self.mana -= 73
        self.mana_spent += 73
        self.hp += 2
        return 2

    def poison(self):
        if self.poison_status > 0:
            raise GamePathDeadError("This status effect is already active") from None
        self.poison_status = 6
        self.mana -= 173
        self.mana_spent += 173
        return 0

    def shield(self):
        if self.shield_status > 0:
            raise GamePathDeadError("This status effect is already active") from None
        self.shield_status = 6
        self.mana -= 113
        self.mana_spent += 113
        return 0

    def recharge(self):
        if self.recharge_status > 0:
            raise GamePathDeadError("This status effect is already active") from None
        self.recharge_status = 5
        self.mana -= 229
        self.mana_spent += 229
        return 0

    def player_turn(self):
        if self.hard_mode:
            self.hp -= 1
            if self.hp <= 0:
                raise GamePathDeadError("You are dead") from None

        if self.poison_status > 0:
            self.poison_status -= 1
            self.boss_hp -= self.poison_damage

        if self.shield_status > 0:
            self.shield_status -= 1

        if self.recharge_status > 0:
            self.recharge_status -= 1
            self.mana += self.recharge_amount

        if len(self.spell_list) == 0:
            raise OutOfSpellsError("Out of spells") from None
        match self.spell_list[0]:
            case "missile":
                self.boss_hp -= self.missile()
            case "drain":
                self.boss_hp -= self.drain()
            case "poison":
                self.poison()
            case "shield":
                self.shield()
            case "recharge":
                self.recharge()

        if self.mana < 0:
            raise GamePathDeadError("Out of mana") from None

        self.spell_list.pop(0)

    def boss_turn(self):
        if self.poison_status > 0:
            self.poison_status -= 1
            self.boss_hp -= self.poison_damage
        if self.shield_status > 0:
            self.shield_status -= 1
        if self.recharge_status > 0:
            self.recharge_status -= 1
            self.mana += self.recharge_amount
        if self.boss_hp > 0:
            self.hp -= (
                self.boss_dmg
                if self.shield_status == 0
                else self.boss_dmg - self.shield_armor
            )
            if self.hp <= 0:
                raise GamePathDeadError("You are dead") from None


class GamePathDeadError(Exception):
    pass


class OutOfSpellsError(Exception):
    pass


def simulate(input, tested, spell_list, spells, hard_mode):
    for s in spell_list:
        tmp = list(spells) + [s]
        try:
            g = game(input, list(tmp), hard_mode)
            i = 0
            while True:
                if g.boss_hp <= 0:
                    tested.add(g.mana_spent)
                    break
                if i % 2 == 0:
                    g.player_turn()
                else:
                    g.boss_turn()
                if len(tested) > 0 and g.mana_spent >= max(tested):
                    break
                i += 1
        except OutOfSpellsError:
            simulate(input, tested, spell_list, tmp, hard_mode)
        except GamePathDeadError:
            pass
        except RecursionError:
            pass


def part_one(input: str, test_run=False):
    # Drain is useless for my input, and slows execution by order of magnitude
    spell_list = ["recharge", "poison", "shield", "missile"]
    tested = set()
    simulate(input, tested, spell_list, list(), False)
    return min(tested)


def part_two(input: str, test_run=False):
    # Drain is useless for my input, and slows execution by order of magnitude
    spell_list = ["recharge", "poison", "shield", "missile"]
    tested = set()
    simulate(input, tested, spell_list, list(), True)
    return min(tested)
