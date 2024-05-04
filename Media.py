class Media:
    def __init__(self, title=None, status=None, requestedBy=None):
        self.title = title
        self.status = status
        self.requestedBy = requestedBy

    def __str__(self):
        return f"Title: {self.title}\nStatus: {self.status}"
    
    def fromDict(self, d):
        for k, v in d.items():
            setattr(self, k, v)

    def toDict(self):
        return self.__dict__