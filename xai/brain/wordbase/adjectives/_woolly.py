

#calss header
class _WOOLLY():
	def __init__(self,): 
		self.name = "WOOLLY"
		self.definitions = [u'made of wool, or made of something that looks like wool: ', u'Woolly ideas and thinking are confused and not clear, and have not been considered carefully enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
