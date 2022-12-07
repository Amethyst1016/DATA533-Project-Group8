class Topic:
    topics = [] # store all topics
    def __init__(self, tname, user):
        self.tname = tname
        self.tag=""
        if tname not in self.topics:
            self.topics.append(self)
            self.user = user
    def addtag(self, tag):
        self.tag = tag
    def related(self):
        related = []
        if self.tag:
            for i in self.topics:
                if i.tag == self.tag:
                    related.append(i.tname)
            if len(related) == 0:
                return "Currently no related topics."
            else: return related
        else:
            return "This topic haven't been taged."