class TopicMapReduce:
    def __init__(self):
        self.x = dict()
    def map(self, word):
        if word not in self.x:
            self.x[word] = 1
        else:
            self.x[word] += 1
    def reduce(self):
        cnt = 0
        for k, v in sorted(self.x.items(), key=lambda item: -item[1]):
            yield k, v
            if cnt == 30:
                break
