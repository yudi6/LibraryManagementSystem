from Library import Library
from ui.UI import UI

if __name__ == '__main__':
    system = Library(host="localhost", user="root", pwd="MySQL")
    our_ui = UI(system)
