import csv
import json
import xml.etree.ElementTree as ET

class CSVtoJSONAdapter:
    '''Convert CSV to JSON'''
    def __init__(self, csv_file, output_json_file):
        self.csv_file = csv_file
        self.output_json_file = output_json_file

    def convert(self):
        with open(self.csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]

        with open(self.output_json_file, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"The file '{self.csv_file}' was successfully converted to the '{self.output_json_file}' one.")

        # Возвращаем название JSON файла вместо данных
        return self.output_json_file


csv_to_json = CSVtoJSONAdapter('csv.csv', 'csv->json.json')
json_file_name = csv_to_json.convert()


class JSONtoCSVAdapter:
    '''Convert JSON to CSV'''
    def __init__(self, json_file_name):
        self.json_file_name = json_file_name

    def convert(self, output_csv_file):
        with open(self.json_file_name, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(data)

        # Выводим имя файла
        print(f"The file '{self.json_file_name}' was successfully converted to the '{output_csv_file}' one.")


# Используем название файла вместо содержимого
JSONtoCSVAdapter(json_file_name).convert('json->csv.csv')


class XMLtoJSONAdapter:
    '''Convert XML to JSON'''
    def __init__(self, xml_file, output_json_file_2):
        self.xml_file = xml_file
        self.output_json_file_2 = output_json_file_2

    def convert(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        def xml_to_dict(element):
            result = {}
            for child in element:
                if len(child) > 0:
                    child_dict = xml_to_dict(child)
                else:
                    child_dict = child.text

                if child.tag in result:
                    if not isinstance(result[child.tag], list):
                        result[child.tag] = [result[child.tag]]
                    result[child.tag].append(child_dict)
                else:
                    result[child.tag] = child_dict
            return result

        data = {root.tag: xml_to_dict(root)}

        with open(self.output_json_file_2, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"The file '{self.xml_file}' was successfully converted to the '{self.output_json_file_2}' one.")

        # Возвращаем название JSON файла вместо данных
        return self.output_json_file_2


xml_to_json = XMLtoJSONAdapter('xml.xml', 'xml->json.json')
json_file_name_from_xml = xml_to_json.convert()
# Вывод имени файла вместо содержимого JSON
print(f"JSON data is stored in file: '{json_file_name_from_xml}'")
