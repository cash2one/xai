

#calss header
class _PLUNK():
	def __init__(self,): 
		self.name = "PLUNK"
		self.definitions = [u'making a hollow sound like that made when an object is dropped heavily onto a surface: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
