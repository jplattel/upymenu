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

# Create a menut and some options
menu = Menu("menu")
sub_menu = Menu("submenu")
noop_menu = MenuNoop("noop")
action_menu = MenuAction("action", lambda: "action")
menu.add_option(sub_menu)
menu.add_option(action_menu)
menu.add_option(noop_menu)

# Test menu instance
assert menu.title == 'menu'

# Test the start of the menu, with a mocked LCD
menu.start(MockLCD(16, 2))
assert len(menu.options) == 3
assert menu.options[0].title == 'submenu'
assert len(menu.options_chunked) == 2
assert len(menu.options_chunked[0]) == 2

# Test focus
assert menu.focus == 1
menu.focus_next()
assert menu.focus == 2
menu.focus_prev()
assert menu.focus == 1

# Test wrap around
menu.focus_next()
menu.focus_next()
menu.focus_next()
assert menu.focus == 1

# And wrap around from the start
menu.focus_prev()
assert menu.focus == 3

# Test submenu
menu.focus_next() # The first item is the submenu
assert menu.focus == 1
menu = menu.choose() 
assert menu.title == 'submenu'
assert menu.options == []

# And move back up the tree once again
menu = menu.parent()
assert menu.title == 'menu'