from functools import lru_cache, partial, reduce, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    # Operations allowed to choose as 'operation' parameter
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError("Unknown operation")

    return reduce(operations[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Cast {element} with power {power} on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    d_ret = {"fire": partial(base_enchantment, 50, "Fire"),
             "water": partial(base_enchantment, 50, "Water"),
             "earth": partial(base_enchantment, 50, "Earth")
             }
    return d_ret


# Accumulates the cache of the results already returned
@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Error: n must be >= 0")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
# The cache can be checked with:
#   memoized_fibonacci.cache_info()


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    spell_powers = [46, 29, 17, 26, 15, 24]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [17, 19, 20]

    print("Testing spell reducer...")
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"]("Sword"))
    print(enchantments["water"]("Shield"))
    print(enchantments["earth"]("Hammer"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    spell = spell_dispatcher()

    print("\nTesting spell dispatcher...")
    print(spell(42))
    print(spell("fireball"))
    print(spell([1, 2, 3]))
