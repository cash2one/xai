

#calss header
class _ENAMOURED():
	def __init__(self,): 
		self.name = "ENAMOURED"
		self.definitions = [u'liking something a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
