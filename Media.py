class Media:
    def __init__(self, title=None, status=None):
        if title != None:
            self.title = title.lower()
        if status != None:
            self.status = status.lower()

    def __str__(self):
        return f"Title: {self.title}\nStatus: {self.status}"
    
    def fromDict(self, d):
        for k, v in d.items():
            setattr(self, k, v)

    def toDict(self):
        return self.__dict__