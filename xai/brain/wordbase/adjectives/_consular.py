

#calss header
class _CONSULAR():
	def __init__(self,): 
		self.name = "CONSULAR"
		self.definitions = [u'relating to a consul or a consulate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
