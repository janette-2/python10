from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrap(*args, **kwargs):
        # Before code------
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        # *args = tuple with all the arguments
        # **kwargs = dict with all the variables (keys ej:(key="value"))
        #  and respective values of the arguments
        result = func(*args, **kwargs)
        # After code-------
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrap


# Adaptable to different functions
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    # Tries to execute a function ended in Exception for max_attempts
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying ... (attempt {attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


#class MageGuild:
    #@staticmethod
    #def validate_mage_name(name: str) -> bool
    #def cast_spell(self, spell_name: str, power: int) -> str


if __name__ == "__main__":

    test_powers = [30, 12, 5, 16]
    spell_names = ['heal', 'freeze', 'meteor', 'darkness']
    mage_names = ['Rowan', 'Jordan', 'Casey', 'Nova', 'River', 'Morgan']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting power validator...")

    @power_validator(10)
    def cast_spell(power, spell_name):
        return f"Successfully cast {spell_name} with {power} power"

    print(cast_spell(test_powers[0], spell_names[-1]))
    print(cast_spell(test_powers[2], spell_names[-2]))

    print("\nTesting retry spell...")

    # Function that provokes errors to force the retry:

    @retry_spell(3)
    def provoke_error():
        raise ValueError("Forced error")
    print(provoke_error())
    print("Waaaaaaagh spelled !")
