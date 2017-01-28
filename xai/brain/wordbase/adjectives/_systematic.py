

#calss header
class _SYSTEMATIC():
	def __init__(self,): 
		self.name = "SYSTEMATIC"
		self.definitions = [u'according to an agreed set of methods or organized plan: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
