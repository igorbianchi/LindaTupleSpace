class Linda:
    def __init__(self):
        self.tupleSpace = {}
    # adds tuple to tuple space
    def _out(self, thread, author, data):
        if(self.tupleSpace.get(thread)):
            self.tupleSpace[thread].append({"author": author, "data": data})
            return "A thread was updated"
        else:
            self.tupleSpace[thread] = []
            self.tupleSpace[thread].append({"author": author, "data": data})
            return "A new thread was created"
    # attemps to match some tuple in tuple space, if a match is found, removes from tuple space
    def _in(self, thread, author, data):
        removed = False
        for x in range(0, self.tupleSpace[thread].__len__()):
            if(self.tupleSpace[thread][x]["author"] == author and self.tupleSpace[thread][x]["data"] == data):
               removed = self.tupleSpace[thread][x]
               self.tupleSpace[thread].pop(x)
               break
        if(not removed):
            return "Not removed, invalid tuple"
        else:
            return str(removed)
    # similar to in except that the matched tuple remains in tuple space
    # the esecuting process suspends if it fails to match a tuple
    def _rd(self, thread):
        if(self.tupleSpace.get(thread)):
            return str(self.tupleSpace[thread])
        else:
            return "Failed to return thread"
