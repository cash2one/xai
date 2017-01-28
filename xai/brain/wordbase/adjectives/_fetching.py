

#calss header
class _FETCHING():
	def __init__(self,): 
		self.name = "FETCHING"
		self.definitions = [u'A fetching person or piece of clothing is attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
