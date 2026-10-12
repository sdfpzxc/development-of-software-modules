from rich.console import Console
from app.services.calculator import calculate_average, calculate_min, calculate_max
from app.utils.formatter import format_report


def main():
    values = [5, 4, 5, 3, 5]
    average = calculate_average(values)
    minimum = calculate_min(values)
    maximum = calculate_max(values)

    report = format_report(average, minimum, maximum)

    console = Console()
    console.print(f"[bold green]{report}[/bold green]")


if __name__ == "__main__":
    main()