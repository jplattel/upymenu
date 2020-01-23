from upymenu import Menu, MenuAction, MenuNoop

class MockLCD():
    def __init__(self, num_columns, num_lines):
        self.num_columns = num_columns
        self.num_lines = num_lines
        self.screen = []

    def clear(self):
        self.screen = []

    def move_to(self, x, y):
        return
    
    def putstr(self, s):
        return s

menu = Menu("test")

assert menu.title == 'test'
assert len(menu.options) == 0

sub_menu = Menu("submenu")
menu.add_option(sub_menu)

assert len(menu.options) == 1
assert menu.options[0].title == 'submenu'

menu.start(MockLCD(16, 2))

assert len(menu.options_chunked) == 1
assert len(menu.options_chunked[0]) == 1
