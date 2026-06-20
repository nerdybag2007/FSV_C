def electricity_bill(units: int) -> int:
    """Calculate electricity bill with slab rates:
    - First 100 units: 5 rupees/unit
    - Next 100 units: 7 rupees/unit
    - Remaining units: 10 rupees/unit
    """
    if units < 0:
        raise ValueError("Units cannot be negative")

    first_slab = min(units, 100)
    remaining = max(units - 100, 0)

    second_slab = min(remaining, 100)
    remaining = max(remaining - 100, 0)

    third_slab = remaining

    return first_slab * 5 + second_slab * 7 + third_slab * 10


def main() -> None:
    units = int(input("Enter units consumed: ").strip())
    total = electricity_bill(units)
    print(f"Electricity bill: {total} rupees")


if __name__ == "__main__":
    main()

