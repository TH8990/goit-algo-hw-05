import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """Парсить один рядок логу та повертає словник."""
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2].upper(),
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу та повертає список словників логів."""
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує записи логів за певним рівнем."""
    return list(filter(lambda log: log.get('level') == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів логів за рівнем."""
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

def display_log_counts(counts: dict):
    """Відображає кількість логів у відформатованій таблиці."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16}| {count}")

def main():
    """Основна функція для запуску скрипта аналізу логів."""
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [level]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()