# uPyMenu

uPyMenu is a micropython menu implementation for LCD displays. Coming from an Arduino experience, I was used with LiquidDisplay and LiquidMenu, but they don't offer a python implementation. So I figured I could create one myself.

# Development

Current development is done based on when I have to to work on it when I want to. But feel free to fork it and add your functionality. If you find any bugs or have suggestions for features, please open up a issue (or pull-request if you create the feature yourself!).

# Usage

The example below renders a menu with a submenu and actions that have callbacks attached which you can use to run your own function. It requires one dependency, and that's `python_lcd` for interacting with the LCD itself.

```python
from upymenu import Menu, MenuAction

def action_callback(event):
    print(event)

submenu = Menu("Submenu")
submenu_action_1 = MenuAction("Submenu Action", callback=action_callback)
submenu_action_2 = MenuAction("Submenu Action 1", callback=action_callback)
submenu.add_option(submenu_action_1)
submenu.add_option(submenu_action_2)

menu_action = MenuAction("Action", callback=action_callback)
menu = Menu("Main Menu")

menu.add_option(submenu)
menu.menu_action(submenu)

menu.render() # Renders the menu on the LCD
```

# Testing

TBD.