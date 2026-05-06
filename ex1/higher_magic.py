from collections.abc import Callable


def spell_1(target: str, power: int) -> str:
    return f"Spell1 takes {target} for {power}"


def spell_2(target: str, power: int) -> str:
    return f"Spell2 takes {target} for {power}"


def spell_3(target: str, power: int) -> str:
    return f"Spell3 takes {target} for {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_condition(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast_condition


# Condition to pass
def enough_power(target: str, power: int) -> bool:
    return power >= 20


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_spells(target: str, power: int) -> list[str]:
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return cast_spells


if __name__ == "__main__":
    # Higher Realm Test Data
    # Use these in your test functions:
    test_values = [16, 16, 17]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    # Declaring functions
    spell1_s = spell_1
    spell_2_s = spell_2

    print("Testing spell combiner...")
    comb_s = spell_combiner(spell1_s, spell_2_s)
    print("Combined spell result:", end="")
    c_res = comb_s(test_targets[0], test_values[0])
    print(f" {c_res[0]}, {c_res[1]}")

    print("\nTesting power amplifier...")
    pow_s = power_amplifier(spell1_s, 2)
    print(f"Original: {test_values[0]}, Amplified: {2 * test_values[0]}")
    print(pow_s(test_targets[0], test_values[0]))

    print("\nTesting conditional caster...")
    cond_cast = conditional_caster(enough_power, spell1_s)
    # False condition (!>=20)
    print(cond_cast(test_targets[1], test_values[1]))
    # True condition
    print(cond_cast(test_targets[1], 20))

    print("\nTesting spell sequence...")
    seq_spell = spell_sequence([spell_1, spell_2, spell_3])
    print(seq_spell(test_targets[2], test_values[2]))
