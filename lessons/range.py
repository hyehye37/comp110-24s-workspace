"""Demosntrates range in a for loop."""


names: list[str] = ["Alyssa", "Vrinda", "Janet"]

for idx in range (0, len(names)):
    print(f"{idx}: {names[idx]}")
