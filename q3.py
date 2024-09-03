import json
import xml.etree.ElementTree as ET


def load_with_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(e)


def load_with_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = [{"dia": int(row.find('dia').text), "valor": float(row.find('valor').text)} for row in root.findall('row')]
        return data
    except ET.ParseError as e:
        print(e)


def process_data(data):
    revenue = [day['valor'] for day in data if day['valor'] > 0]

    min_revenue = min(revenue)
    max_revenue = max(revenue)

    monthly_average = sum(revenue) / len(revenue)

    days_above_average = sum(1 for value in revenue if value > monthly_average)

    print(f"Minimum revenue: {min_revenue:.2f}")
    print(f"Maximum revenue: {max_revenue:.2f}")
    print(f"Number of days with revenue above the average: {days_above_average}")


choice = input("Choose format data extraction\n1 - JSON | 2 - XML\nChoice: ")

if choice == "1":
    data = load_with_json('raw_data/dados.json')
elif choice == "2":
    data = load_with_xml('raw_data/dados (2).xml')
else:
    choice = None
    print("Invalid choice. Ending Program!")

if choice is not None:
    process_data(data)
