

#calss header
class _FLIMSY():
	def __init__(self,): 
		self.name = "FLIMSY"
		self.definitions = [u'very thin, or easily broken or destroyed: ', u'A flimsy argument, excuse, etc. is weak and difficult to believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
