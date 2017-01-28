

#calss header
class _SMALL():
	def __init__(self,): 
		self.name = "SMALL"
		self.definitions = [u'little in size or amount when compared with what is typical or average: ', u'A small child is a very young child that is older than a baby: ', u'limited in the amount of an activity: ', u'not very important or not likely to cause problems: ', u'ashamed or weak: ', u'Small letters are not capital letters: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
