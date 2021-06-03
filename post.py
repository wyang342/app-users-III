class Post:
    def __init__(self, **kwargs):
        self.title = kwargs["title"]
        self.date = kwargs["date"]
        self.desc = kwargs["desc"]
        self.author = kwargs["author"]
