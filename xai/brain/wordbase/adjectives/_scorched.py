

#calss header
class _SCORCHED():
	def __init__(self,): 
		self.name = "SCORCHED"
		self.definitions = [u'slightly burned, or damaged by fire or heat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
