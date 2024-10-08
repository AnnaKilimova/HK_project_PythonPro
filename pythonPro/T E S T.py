import xml.etree.ElementTree as ET

def load_books(file_path):
    """Чтение данных из XML-файла"""
    try:
        tree = ET.parse(file_path)
        return tree
    except FileNotFoundError:
        print(f"File {file_path} is not found!")
        return None

def list_available_books(root):
    """Вывод списка доступных продуктов"""
    if root is None:
        return
    print("Available products:")
    for product in root.findall('product'):
        name = product.find('name').text
        quantity = product.find('quantity').text
        print(f"- {name}: {quantity} units available")

def add_book(root, name, price, quantity):
    """Добавление нового продукта в XML"""
    # Создаем новый элемент продукта
    new_product = ET.Element("product")
    ET.SubElement(new_product, "name").text = name
    ET.SubElement(new_product, "price").text = str(price)
    ET.SubElement(new_product, "quantity").text = str(quantity)

    # Добавляем новый продукт в корень
    root.getroot().append(new_product)

def save_books(tree, file_path):
    """Сохранение изменений в XML-файл"""
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    file_path = "data.xml"

    # Чтение книг из файла
    tree = load_books(file_path)
    if tree is not None:
        root = tree.getroot()

        # Вывод доступных продуктов
        list_available_books(root)

        # Получение информации о новом продукте
        new_book_name = input("Enter the name of the new product: ")
        new_book_price = input("Enter the price of the product: ")
        new_book_quantity = input("Enter the quantity of the product: ")

        # Добавление нового продукта
        add_book(tree, new_book_name, new_book_price, new_book_quantity)

        # Сохранение изменений
        save_books(tree, file_path)

        print(f"The product '{new_book_name}' has been successfully added.")

