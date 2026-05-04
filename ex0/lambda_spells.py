def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        # List to sort
        artifacts,
        # Sorts by extracting the value of 'power' of each dict in the list
        key=lambda artifact: artifact["power"],
        # Higher to lower
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages)
            )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(
        map(lambda spell: f"* {spell} *",
            spells)
    )


def mage_stats(mages: list[dict]) -> dict:
    # Returns the dict with the max power
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(sum(mage["power"] for mage in mages) / len(mages), 2)
    return {"max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power
            }


if __name__ == "__main__":

    artifacts = [{'name': 'Wind Cloak', 'power': 105, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 71, 'type': 'armor'},
                 {'name': 'Storm Crown', 'power': 118, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 66, 'type': 'armor'}]

    mages = [{'name': 'River', 'power': 59, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 96, 'element': 'shadow'},
             {'name': 'Jordan', 'power': 75, 'element': 'shadow'},
             {'name': 'Zara', 'power': 53, 'element': 'water'},
             {'name': 'Rowan', 'power': 100, 'element': 'ice'}]
    spells = ['shield', 'blizzard', 'fireball', 'lightning']

    print("Testing artifact sorter...")
    sorted_l = artifact_sorter(artifacts)
    print(f"{sorted_l[0]["name"]} {sorted_l[0]["type"]}"
          f" ({sorted_l[0]["power"]} power) comes before"
          f" {sorted_l[1]["name"]} {sorted_l[1]["type"]}"
          f" ({sorted_l[1]["power"]} power)")

    print("\nTesting power filter...")
    pwr_l = power_filter(mages, 90)
    print("The ones that overpass the minimum are:")
    for i in pwr_l:
        print(f"{i["name"]} {i["element"]}"
              f" ({i["power"]} power)")

    print("\nTesting spell transformer...")
    spell_l = spell_transformer(spells)
    print(f"{" ".join(spell_l)}")

    print("\nTesting mage stats...")
    stats_d = mage_stats(artifacts)
    print(f"Max: {stats_d["max_power"]}, Min: {stats_d["min_power"]},"
          f" Avg: {stats_d["avg_power"]}")
