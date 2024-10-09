'''Додаткові завдання (реалізація паттерна "Адаптер" (Adapter)):
1) Перетворення між форматами:
• Реалізуй класи, які перетворюватимуть CSV-файл до JSON та навпаки.
• Додай функціонал для перетворення XML-файлу до JSON.
2) Уяви, що ти розробляєш систему для відправки повідомлень різними каналами: через SMS, Email та Push-повідомлення.
Усі ці канали мають різні інтерфейси для відправки повідомлень, але ти хочеш уніфікувати їх,
щоб використовувати один універсальний інтерфейс для відправки повідомлень незалежно від каналу.
• Створи інтерфейс MessageSender, який визначає метод для відправки повідомлення:
3) Є три класи, кожен з яких реалізує власний метод для відправки повідомлень:
• SMSService: має метод send_sms(phone_number, message).
• EmailService: має метод send_email(email_address, message).
• PushService: має метод send_push(device_id, message).
Створи ці класи з відповідними методами для відправки повідомлень.
4) Для кожного з класів (SMSService, EmailService, PushService) створи окремі адаптери, які будуть реалізовувати інтерфейс
MessageSender. Адаптери мають використовувати відповідні методи існуючих класів для відправки повідомлень:
• SMSAdapter: адаптує SMSService для використання через інтерфейс MessageSender.
• EmailAdapter: адаптує EmailService.
• PushAdapter: адаптує PushService.
5) Напиши код, який створює екземпляри адаптерів для кожного типу сервісу (SMS, Email, Push) та відправляє повідомлення
за допомогою універсального інтерфейсу MessageSender.
6) Реалізуй систему відправки повідомлень, яка приймає список адаптерів і відправляє одне і те ж повідомлення через усі
доступні сервіси.
7) Додай обробку помилок для кожного сервісу, якщо відправка повідомлення не вдалася.
OЧIКУВАНИЙ РЕЗУЛЬТАТ: код має уніфікувати процес відправки повідомлень через різні сервіси, дозволяючи використовувати
один загальний інтерфейс для роботи з різними типами повідомлень.
'''


import csv
import json
import xml.etree.ElementTree as ET


# CONVERT BETWEEN FORMATS:


class CSVtoJSONAdapter:
    """Convert CSV to JSON."""

    def __init__(self, csv_file, output_json_file):
        """
        :param csv_file: input CSV file name.
        :param output_json_file: output JSON file name.
        """
        # The fields store the paths to the files.
        self.csv_file = csv_file
        self.output_json_file = output_json_file

    def convert(self):
        """Opens the CSV file for reading."""
        with open(self.csv_file, mode="r", encoding="utf-8") as file:
            # Reads CSV and represents strings as dictionaries.
            csv_reader = csv.DictReader(file)
            # The list of dictionaries is stored in the variable data.
            data = [row for row in csv_reader]

        with open(self.output_json_file, mode="w", encoding="utf-8") as json_file:
            # A JSON file is opened for writing.
            # Data from data is written to an indented (4 spaces) JSON file, with support for
            # non-ASCII characters (ensure_ascii=False).
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"The file '{self.csv_file}' was successfully converted to the '{self.output_json_file}' one.")

        # The name of the JSON output file is returned, allowing it to be used in other parts of the programme.
        return self.output_json_file


# An object is created to convert the file.
csv_to_json = CSVtoJSONAdapter("csv.csv", "csv->json.json")
# The conversion is performed using the convert method, and the JSON filename is returned.
json_file_name = csv_to_json.convert()


class JSONtoCSVAdapter:
    """Convert JSON to CSV"""

    # The constructor takes the name of the input JSON file and stores it in the
    # self.json_file_name field.
    def __init__(self, json_file_name):
        self.json_file_name = json_file_name

    def convert(self, output_csv_file):
        """The convert method opens a JSON file for reading and loads its contents into
        the data variable using json.load."""
        with open(self.json_file_name, mode="r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        with open(output_csv_file, mode="w", newline="", encoding="utf-8") as file:
            # Opens a CSV file for writing.
            # Writes headers (keys from the dictionary) and rows of data to the CSV file.
            csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
            csv_writer.writeheader()  # Writes the table header.
            csv_writer.writerows(data)  # Writes the rows.

        print(f"The file '{self.json_file_name}' was successfully converted to the '{output_csv_file}' one.")


# An object is created to convert a JSON file to CSV and the conversion is performed.
JSONtoCSVAdapter(json_file_name).convert("csv.csv")


class XMLtoJSONAdapter:
    """Convert XML to JSON"""

    # The constructor takes the name of the XML file and the name of the output JSON file
    # and stores them in the appropriate fields.
    def __init__(self, xml_file, output_json_file_2):
        self.xml_file = xml_file
        self.output_json_file_2 = output_json_file_2

    def convert(self):
        tree = ET.parse(self.xml_file)  # Parses the XML file.
        root = (tree.getroot())  # Retrieves the root element of the XML structure.

        def xml_to_dict(element):
            # Recursively converts an XML element into a dictionary.
            result = {}
            for child in element:
                # If the element has children, recursion is invoked.
                if len(child) > 0:
                    child_dict = xml_to_dict(child)
                # If the element doesn't have children, the text content is saved.
                else:
                    child_dict = child.text
                # Duplicate tags are merged into the list.
                if child.tag in result:
                    if not isinstance(result[child.tag], list):
                        result[child.tag] = [result[child.tag]]
                    result[child.tag].append(child_dict)
                else:
                    result[child.tag] = child_dict
            return result

        # Converting an XML root element to a dictionary.
        data = {root.tag: xml_to_dict(root)}

        # The output JSON file is opened and data is written to it.
        with open(self.output_json_file_2, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"The file '{self.xml_file}' was successfully converted to the '{self.output_json_file_2}' one.")

        # The name of the JSON output file is returned.
        return self.output_json_file_2


# An object is created to convert the XML file to JSON.
xml_to_json = XMLtoJSONAdapter("xml.xml", "xml->json.json")
# The conversion is performed.
json_file_name_from_xml = xml_to_json.convert()

print()

# THE INTERFACE THAT DEFINES A METHOD FOR SENDING A MESSAGE:


class MessageSender:
    """Defines the method for sending the message"""

    def send_messages(self, message: str):
        pass


# CLASSES FOR SENDING MESSAGES:
class SMSService:
    def send_sms(self, phone_number, message):
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    def send_email(self, email_address, message):
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    def send_push(self, device_id, message):
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


# ADAPTERS FOR IMPLEMENTING THE MessageSender INTERFACE:


class SMSAdapter(MessageSender):
    def __init__(self, sms_service: SMSService, phone_number: str):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        self.sms_service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    def __init__(self, email_service: EmailService, email_address: str):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        self.email_service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    def __init__(self, push_service: PushService, device_id: str):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        self.push_service.send_push(self.device_id, message)


if __name__ == "__main__":
    # Creating services
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()

    # Creating adapters for each service
    sms_adapter = SMSAdapter(sms_service, "+380123456789")
    email_adapter = EmailAdapter(email_service, "user@example.com")
    push_adapter = PushAdapter(push_service, "device123")

    adapters = [sms_adapter, email_adapter, push_adapter]

    # Sending messages through various services using adapters
    message = "Привіт! Це тестове повідомлення."

    # We use a universal interface for sending messages
    # sms_adapter.send_message(message)
    # email_adapter.send_message(message)
    # push_adapter.send_message(message)


# Error handling if sending a message fails.
def send_message_to_all(adapters: list, message: str):
    for adapter in adapters:
        try:
            adapter.send_message(message)  # Call send_message for each adapter
        except Exception as e:
            print(f"Помилка під час відправки повідомлення через {adapter.__class__.__name__}: {e}")


send_message_to_all(adapters, message)
