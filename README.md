# uPyMenu

uPyMenu is a micropython menu implementation for LCD displays. Coming from an Arduino experience, I was used with [LiquidCrystal](https://github.com/arduino-libraries/LiquidCrystal) and [LiquidMenu](https://github.com/VaSe7u/LiquidMenu), but they don't offer a python implementation. So I figured I could create one myself.

# Development

Current development is done based on when I have to to work on it when I want to. But feel free to fork it and add your functionality. If you find any bugs or have suggestions for features, please open up a issue (or pull-request if you create the feature yourself!).

# Usage

The example below renders a menu with a submenu and actions that have callbacks attached which you can use to run your own function. It requires one dependency, and that's [`python_lcd`](https://github.com/dhylands/python_lcd) for interacting with the LCD itself.

```python
from machine import Pin, I2C # Basics for creating an LCD interface
from esp8266_i2c_lcd import I2cLcd # Example LCD interface used
from upymenu import Menu, MenuAction, MenuNoop

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
menu.add_option(menu_action)
menu.add_option(MenuNoop("Nothing here"))

# Example config for LCD via i2c, you will need this 
# for the menu to function, the screen size is required
# to render the menu correctly on the screen.
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x3F, 4, 20)

current_menu = menu.start(lcd) # Starts the menu on the LCD

menu.focus_next() # Focus on the next item in the menu 
menu.focus_prev() # Focus on the previous item in the menu 

# Choose the focused item, if it's and action execute 
# the callback, or if it is a menu, render that menu.
current_menu = menu.choose() 

# If it's a submenu, you can use the parent() function
# to navigate back up to the tree.
current_menu = menu.parent() 
```

# Testing

TBD.