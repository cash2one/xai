

#calss header
class _GLADIATORIAL():
	def __init__(self,): 
		self.name = "GLADIATORIAL"
		self.definitions = [u'relating to violent fighting in which only one person or group can win: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
