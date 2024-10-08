'''Завдання 5: Робота з XML
1. Створи XML-файл, що містить інформацію про продукти магазину:
• Назва продукту • Ціна • Кількість на складі
2.Напиши програму, яка:
• Читає XML-файл і виводить назви продуктів та їхню кількість. • Змінює кількість товару та зберігає зміни в XML-файл.'''


import xml.etree.ElementTree as ET

def load_products(file_path):
    """Loads an XML file and returns its root element."""
    try:
        # Parses (analyses) the XML file and creates a tree structure representing the XML document.
        tree = ET.parse(file_path)
        # Returns the root element of the XML document.
        # Two values are returned: the root element and the tree itself for saving changes later.
        return tree.getroot(), tree
    # An error is handled if the file at the specified path is not found.
    # In this case, an error message is output and the function returns None.
    except FileNotFoundError:
        print(f"The {file_path} file has not been found!")
        return None, None
    # If the XML file is corrupted or cannot be correctly recognised,
    # a parsing problem message is displayed and the function returns None.
    except ET.ParseError:
        print(f"Error parsing XML file {file_path}!")
        return None, None

def list_products(root):
    """This function takes a root element and outputs a list of products and their quantity in stock."""

    # If root is None, the function terminates because this indicates that the XML data is missing or corrupted
    if root is None:
        return
    print("The list of the products:")
    # The for loop loops through all <product> elements found in the XML file.
    for product in root.findall('product'):
        # Looks inside each <product> element for the <name> tag and extracts its textual content (product name).
        name = product.find('name').text
        # retrieves the amount of product in stock
        quantity = product.find('quantity').text
        print(f"- {name}: {quantity} на складі")

def update_product_quantity(root, product_name, new_quantity):
    """Updates the product quantity for a specific product if the product name matches the one entered by the user."""

    product_name = product_name.strip().lower()  # Remove extra spaces and convert to lower case
    for product in root.findall('product'):
        name = product.find('name').text.strip().lower()  # Lowercase for comparison purposes
        if name == product_name:
            product.find('quantity').text = str(new_quantity)
            print(f"The quantity of the '{product_name}' product was changed to {new_quantity}.")
            return True
    print(f"`The product`'{product_name}' is not found.")
    # If the loop completes and no product is found,  the function returns False
    return False

def save_changes(tree, file_path):
    """Saves the changes made in the XML document back to the file."""

    # Saves the XML tree back to the file
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f"Changes are successfully saved to the '{file_path}' file.")

# Checks whether the file is running as a main programme (and not imported as a module).
if __name__ == "__main__":
    file_path = "data.xml"

    # Upload an XML file
    root, tree = load_products(file_path)

    if root is not None:
        # If the file was successfully uploaded, a list of products is displayed.
        list_products(root)

        # Ask the user which product to upgrade
        product_name = input("Enter the product name to update the quantity: ")
        try:
            new_quantity = int(input(f"Enter a new quantity for the '{product_name}' product: "))
        except ValueError:
            print("Error! You must enter a numeric value for the quantity.")
            exit()

        # Update the product quantity
        if update_product_quantity(root, product_name, new_quantity):
            # Saving changes
            save_changes(tree, file_path)
