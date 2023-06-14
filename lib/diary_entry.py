class DiaryEntry:

    already_read = []

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        no_of_words_can_read = wpm * minutes
        diary_entry = self.format()
        split_chunk =  diary_entry.split()[:no_of_words_can_read]
        read_chunk = " ".join(split_chunk)
        if read_chunk in self.already_read:
            raise Exception("You've already read this!")
        self.already_read.append(read_chunk)
        return read_chunk
    
