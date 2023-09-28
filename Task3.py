import csv
from collections import defaultdict
from datetime import datetime

import matplotlib.pyplot as plt


def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def load_csv_data():
    try:
        with open('employees.csv', mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        return data
    except FileNotFoundError:
        print("Помилка: файл 'employees.csv' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


def count_gender(data):
    gender_counts = defaultdict(int)
    for row in data:
        gender = row["Стать"]
        gender_counts[gender] += 1
    return gender_counts


def count_age_categories(data):
    age_categories = defaultdict(int)
    for row in data:
        birthdate = datetime.strptime(row["Дата народження"], '%d.%m.%Y')
        age = calculate_age(birthdate)
        if age < 18:
            category = "Молодший 18"
        elif 18 <= age <= 45:
            category = "18-45"
        elif 45 < age <= 70:
            category = "45-70"
        else:
            category = "Старше 70"
        age_categories[category] += 1
    return age_categories


def count_gender_age_categories(data):
    gender_age_counts = defaultdict(lambda: defaultdict(int))
    for row in data:
        gender = row["Стать"]
        birthdate = datetime.strptime(row["Дата народження"], '%d.%m.%Y')
        age = calculate_age(birthdate)
        if age < 18:
            category = "Молодший 18"
        elif 18 <= age <= 45:
            category = "18-45"
        elif 45 < age <= 70:
            category = "45-70"
        else:
            category = "Старше 70"
        gender_age_counts[gender][category] += 1
    return gender_age_counts


def plot_gender_pie(gender_counts):
    plt.figure(figsize=(8, 8))
    plt.pie(gender_counts.values(), labels=gender_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Розподіл за статтю")
    plt.show()



def main():
    data = load_csv_data()
    if not data:
        return

    gender_counts = count_gender(data)
    age_categories = count_age_categories(data)
    gender_age_counts = count_gender_age_categories(data)

    print("Розподіл за статтю:")
    for gender, count in gender_counts.items():
        print(f"{gender}: {count} співробітників")


    plot_gender_pie(gender_counts)



if __name__ == '__main__':
    main()
