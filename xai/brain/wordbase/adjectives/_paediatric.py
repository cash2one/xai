

#calss header
class _PAEDIATRIC():
	def __init__(self,): 
		self.name = "PAEDIATRIC"
		self.definitions = [u'relating to the medical care of children: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
