from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulator(add: int):
        nonlocal power
        power += add
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    d_res = {}

    def store(key: str, value: str):
        d_res[key] = value

    def recall(key: str) -> str:
        return d_res.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    count_a = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}: {count_a()}")
    count_b = mage_counter()
    print(f"counter_b call 1: {count_b()}")

    print("\nTesting spell accumulator...")
    base1, add1 = (100, 20)
    acc = spell_accumulator(base1)
    print(f"Base {base1}, add {add1}: {acc(add1)}")
    add2 = 30
    print(f"Base {base1}, add {add2}: {acc(add2)}")

    print("\nTesting enchantment factory...")
    enc1 = enchantment_factory("Flaming")
    print(enc1("Sword"))
    enc2 = enchantment_factory("Frozen")
    print(enc1("Shield"))

    print("\nTesting memory vault...")
    d_mem = memory_vault()
    st = d_mem["store"]
    rec = d_mem["recall"]
    print("Store 'secret' = 42")
    st("secret", "42")
    print(f"Recall 'secret': {rec("secret")}")
    print(f"Recall 'unknown': {rec("unknown")}")
