

#calss header
class _NEAT():
	def __init__(self,): 
		self.name = "NEAT"
		self.definitions = [u'tidy, with everything in its place: ', u'Neat people like to keep themselves, their house, and their possessions tidy and in good order: ', u'good: ', u'clever and simple: ', u'(of a strong alcoholic drink) without anything, such as water or ice or another drink, added to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
