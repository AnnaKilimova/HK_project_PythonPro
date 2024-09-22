"""Завдання 5: Календар подій
Розробити простий календар подій.
1. Використовуючи замикання, створити функції для додавання подій, 
   видалення подій та перегляду майбутніх подій.
2. Зберігати події у списку за допомогою глобальної змінної."""

events = []


def events_data():
    def add_event(name):
        events.append(name)
        print(f'The event \'{name}\' is added')

    def remove_event(name):
        if name in events:
            events.remove(name)
            print(f'The event \'{name}\' is removed')
        else:
            print(f'The event \'{name}\' is not found')

    def show_events():
        if events:
            print('All the events: ')
            for number, event in enumerate(events, 1):
                print(f"{number}. {event}")
        else:
            print('The calendar is empty')

    return add_event, remove_event, show_events


add_event, remove_event, show_events = events_data()

add_event("Event_1, time_1")
add_event("Event_2, time_2")
add_event("Event_3, time_3")
remove_event("Event_2, time_2")
remove_event("Event_2")
show_events()
