

#calss header
class _SALARIED():
	def __init__(self,): 
		self.name = "SALARIED"
		self.definitions = [u'being paid a salary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
