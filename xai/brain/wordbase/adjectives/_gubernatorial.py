

#calss header
class _GUBERNATORIAL():
	def __init__(self,): 
		self.name = "GUBERNATORIAL"
		self.definitions = [u'relating to a governor (= the official leader of a state in the US)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
