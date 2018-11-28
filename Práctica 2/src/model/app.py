
class App:

    def __init__(self, line):
        tokens = self.preprocessLine(line)
        self.name = tokens[0]
        self.data = ';'.join(tokens[1:])


    def addReviews(self, comments_list):
        self.comments_str = ";".join( [str(x) for x in comments_list] )

    def preprocessLine(self, line):
        line = line.replace('\n', '')
        return line.split(';')

    def toList(self):
        return [value for (key, value) in self.__dict__.items() if key != 'comments_str']

    def toCSV(self):
        return '{0};{1};{2}\n'.format(self.name, self.data, self.comments_str)
