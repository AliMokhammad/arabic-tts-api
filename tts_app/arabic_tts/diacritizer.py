import mishkal.tashkeel


class Diacritizer:
    def __init__(self, text):
        self.text = text
        
    def add_diacritics(self):
        if not self.text:
                return ""
        
        diacritizer = mishkal.tashkeel.TashkeelClass()
        diac_text = diacritizer.tashkeel(self.text)
        return diac_text
