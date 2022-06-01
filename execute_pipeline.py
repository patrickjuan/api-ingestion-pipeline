from src.handlers.extract_data import main as extract_data
from src.handlers.generate_report import main as generate_report


def main():
    extract_data()
    generate_report()


if __name__ == '__main__':
    main()