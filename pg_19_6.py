# calling functions and methods

def printit():
    print('Opener')

class Message:
    def display(self, msg):
        printit()
        print(msg)

    def show():
        printit()
        print('Hello')
        # display()

printit()
m = Message()
m.display('Good Morning')
Message.show()
