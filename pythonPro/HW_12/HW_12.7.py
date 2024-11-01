"""Завдання 7. Пошук IP-адрес
Напишіть функцію, яка з тексту витягує всі IPv4-адреси. IPv4-адреса складається з чотирьох чисел (від 0 до 255),
розділених крапками."""

import re


def find_ipv4_addresses(text):
    # Template for searching IPv4 address.
    pattern = (
        r"\b(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b"
    )
    # \b - limits the pattern at the word boundary to avoid matches with numbers that only partially match the IP address.
    # (?: ... ) - uses irregular groups to find parts without capturing them for the result.
    # [0-9]{1,2} - corresponds to numbers from 0 to 99.
    # 1[0-9]{2} - corresponds to numbers from 100 to 199.
    # 2[0-4][0-9] - corresponds to numbers from 200 to 249.
    # 25[0-5] - corresponds to numbers from 250 to 255.

    # Finding all the matches.
    ip_addresses = re.findall(pattern, text)
    return ip_addresses


# An example of using the function.
text = "Приклади IP: 192.168.0.1, 255.255.255.255, 10.0.0.1, та некоректна адреса 999.999.999.999"
ips = find_ipv4_addresses(text)
print("Знайдені IP-адреси:", ips)
