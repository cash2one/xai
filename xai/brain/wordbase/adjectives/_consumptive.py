

#calss header
class _CONSUMPTIVE():
	def __init__(self,): 
		self.name = "CONSUMPTIVE"
		self.definitions = [u'(a person) suffering from consumption: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
