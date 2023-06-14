class GrammarStats:

    def __init__(self):
        list_of_passes = []
        self.list_of_passes = list_of_passes
        list_of_fails = []
        self.list_of_fails = list_of_fails

    def check(self, text):
        if text == "":
            raise Exception("Empty string")
        elif text == None:
            raise Exception("No text given")
        elif text[-1] in '!?.' and text.istitle():
            self.list_of_passes.append(text)
            return True 
        else:
            self.list_of_fails.append(text)
            return False
    
    
    def percentage_good(self):
        no_of_texts = len(self.list_of_passes) + len(self.list_of_fails)
        return (len(self.list_of_passes) / no_of_texts) * 100
    
# grammar_stats = GrammarStats()
# grammar_stats.check("Hello!")
# grammar_stats.check("hello")
# print(grammar_stats.percentage_good())