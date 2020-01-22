import math

class Menu:
    def __init__(self, title, render_title=False):
        self.title = title
        self.render_title = render_title # TODO: implement if we should render a title.. can be done, by adding a noop option to the option list?
        self.lcd = lcd
        self.columns = lcd.num_columns
        self.lines = lcd.num_lines
        self.options = []
        self.parent = None
        self.focus = 1 # We start on the first option by default (not 0 to prevent ZeroDivision errors )
        self.viewport = None

    # Chunk the options to only render the ones in the viewport
    def _chunk_options(self):
        for i in xrange(0, len(self.options), self.lcd_lines):
            yield options[i:i + n]

    # Get the current chunk based on the focus position
    def _current_chunk(self):
        return math.floor(self.focus / (self.lines + 1)) # current chunk

    # Starts the menu, used at root level to start the interface.
    def start(self, lcd):
        self.lcd = lcd # Assign the LCD to the menu.

        # Chunk the list and calculate the viewport:
        chunked_options = list(self._chunk_options())
        self.viewport = chunked_menu_options[self._current_chunk()]
        self.render()

    # Renders the menu, also when refreshing (when changing select)
    def render(self):
        self.lcd.clear()
        self.lcd.move_to(0, 0)

        self._render_cursor()

        # Render the options:
        for l, option in enumerate(self.viewport):
            self.lcd.move_to(l, 0) # Move to the line
            # And render the longest possible string on the screen
            self.lcd.putstr(option.title[:self.columns - 1])

    def _render_cursor(self):
        for l in xrange(0, self.lines):
            self.lcd.move_to(l, 0)
            # If the current position matches the focus, render 
            # the cursor otherwise, render an empty space
            if l == (self.focus - 1):
                self.lcd.putstr(">")
            else:
                self.lcd.putstr(" ")

    # Add an option to the menu (could be an action or submenu)
    def add_option(self, option):
        self.options.append(option)

    # Focus on the next option in the menu
    def focus_next(self):
        self.focus += 1
        self.render()

    # Focus on the previous option in the menu
    def focus_prev(self):
        self.focus -= 1
        self.render()

    # Focus on the option n in the menu
    def focus(self, n):
        self.focus = n
        self.render()

    # Choose the item on which the focus is applied
    def choose(self):
        choice = self.options[self.focus]
        print(choice)

    # Navigate to the parent (if the current menu is a submenu)
    def parent():
        if self.parent:
            self.parent.start()

class MenuAction:
    def __init__(self):
        print("action init")
