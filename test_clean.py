from typing import List

def calculate_average(numbers: List[float]) -> float:
    """Calcula el promedio de una lista de numeros."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def format_result(value: float, decimals: int = 2) -> str:
    return f"{value:.{decimals}f}"
