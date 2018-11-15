
class App:

    def __init__(self, line):
        tokens = self.preprocessLine(line)
        print(tokens)
        print(len(tokens))
        self.name        = tokens[0]
        self.category    = tokens[1]
        self.rating      = tokens[2]
        self.reviews     = tokens[3]
        self.size        = tokens[4]
        self.installs    = tokens[5]
        self.type        = tokens[6]
        self.price       = tokens[7]
        self.content     = tokens[8]
        self.rating      = tokens[9]
        self.genres      = tokens[10]
        self.last_update = tokens[11]
        self.current_ver = tokens[12]
        self.android_ver = tokens[13]


    def addReviews(self, comments_list):
        self.comments_str = ",".join( [str(x) for x in comments_list] )

    def preprocessLine(self, line):
        line = line.replace('\n', '')
        return line.split(',')

    def toList(self):
        return [value for (key, value) in self.__dict__.items() if key != 'comments_str']

    def toCSV(self):
        return ",".join( [str(x) for x in self.toList()] ) + '\n'
