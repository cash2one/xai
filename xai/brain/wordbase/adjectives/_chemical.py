

#calss header
class _CHEMICAL():
	def __init__(self,): 
		self.name = "CHEMICAL"
		self.definitions = [u'relating to chemicals: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
