class ToDoList():
    def __init__(self):
        self.to_do_list = ["Walk the dog", "Water the plants"]

    def mark_as_complete(self, task):
        for item in self.to_do_list:
            if item == task:
                self.to_do_list.remove(item)
                self.to_do_list.append(item + " COMPLETED")
                return self.to_do_list
        return self.to_do_list
            
    def remove_completed_task(self):
        for item in self.to_do_list:
            if "COMPLETED" in item:
                self.to_do_list.remove(item)
        return self.to_do_list

    
