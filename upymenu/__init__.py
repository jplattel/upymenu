import math


class Menu:
    def __init__(self, title, render_title=False):
        self.title = title

        # TODO: implement if we should render a title.. can be done, by adding a noop option to the option list?
        self.render_title = render_title
        self.lcd = None
        self.options = []
        self.parent_menu = None

        # We start on the first option by default (not 0 to prevent ZeroDivision errors )
        self.focus = 1
        self.viewport = None
        self.active = False

    # Chunk the options to only render the ones in the viewport
    def _chunk_options(self):
        for i in range(0, len(self.options), self.lines):
            yield self.options[i : i + self.lines]

    # Get the current chunk based on the focus position
    def _current_chunk(self):
        return math.floor(self.focus / (self.lines + 1))  # current chunk

    # Starts the menu, used at root level to start the interface.
    # Or when navigating to a submenu or parten
    def start(self, lcd):
        self.lcd = lcd  # Assign the LCD to the menu.
        self.columns = lcd.num_columns  # Get the columns of the LCD
        self.lines = lcd.num_lines  # And the line
        self.active = True  # Set the screen as active

        # Chunk the list and calculate the viewport:
        self.options_chunked = list(self._chunk_options())
        self.render()
        return self

    # Renders the menu, also when refreshing (when changing select)
    def render(self):
        # We only render the active screen, not the others
        if not self.active or not self.options_chunked:
            return

        self.viewport = self.options_chunked[self._current_chunk()]

        self.lcd.clear()
        self.lcd.move_to(0, 0)

        self._render_cursor()
        self._render_options()

    def _render_cursor(self):
        for l in range(0, self.lines):
            self.lcd.move_to(l, 0)
            # If the current position matches the focus, render
            # the cursor otherwise, render an empty space
            if l == (self.focus - 1):
                self.lcd.putstr(">")
            else:
                self.lcd.putstr(" ")

    def _render_options(self):
        # Render the options:
        for l, option in enumerate(self.viewport):
            self.lcd.move_to(l, 0)  # Move to the line
            # And render the longest possible string on the screen
            self.lcd.putstr(option.title[: self.columns - 1])

    # Add an option to the menu (could be an action or submenu)
    def add_option(self, option):
        if type(option) not in [Menu, MenuAction, MenuNoop]:
            raise Exception(
                "Cannot add option to menu (required Menu, MenuAction or MenuNoop)"
            )
        self.options.append(option)

    # Focus on the next option in the menu
    def focus_next(self):
        self.focus += 1
        # Wrap around
        if self.focus > len(self.options):
            self.focus = 1
        self.render()

    # Focus on the previous option in the menu
    def focus_prev(self):
        self.focus -= 1
        if self.focus < 1:
            self.focus = len(self.options)
        self.render()

    # Focus on the option n in the menu
    def focus_set(self, n):
        self.focus = n
        self.render()

    # Choose the item on which the focus is applied
    def choose(self):
        chosen_option = self.options[self.focus - 1]

        if type(chosen_option) == Menu:
            return self._choose_menu(chosen_option)
        elif type(chosen_option) == MenuAction:
            chosen_option.cb()  # Execute the callback function
            return self
        elif type(chosen_option) == MenuNoop:
            return self

    # Navigate to the parent (if the current menu is a submenu)
    def parent(self):
        if self.parent_menu:
            self.active = False
            return self.parent_menu.start(self.lcd)

    def _choose_menu(self, submenu):
        self.active = False
        submenu.parent_menu = self
        return submenu.start(self.lcd)  # Start the submenu or parent


class MenuAction:
    def __init__(self, title, callback):
        self.title = title
        self.callback = callback

    def cb(self):
        return self.callback()


class MenuNoop:
    def __init__(self, title):
        self.title = title
