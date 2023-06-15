class ToDoList():
    def __init__(self):
        self.to_do_list = []

    def add_to_do(self, to_do):
        self.to_do_list.append(to_do)

    def list_to_dos(self):
        if self.to_do_list == []:
            raise Exception("Nothing to do!")
        else:
            return self.to_do_list