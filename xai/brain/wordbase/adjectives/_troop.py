

#calss header
class _TROOP():
	def __init__(self,): 
		self.name = "TROOP"
		self.definitions = [u'for, relating to, or involving troops: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
