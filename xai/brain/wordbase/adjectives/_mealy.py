

#calss header
class _MEALY():
	def __init__(self,): 
		self.name = "MEALY"
		self.definitions = [u'dry and like a powder: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
