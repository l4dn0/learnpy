from orm import handler
from windows.greetWindow import GreeterWindow

h = handler("database.db")


greeter = GreeterWindow()
greeter.mainloop()