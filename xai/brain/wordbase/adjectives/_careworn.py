

#calss header
class _CAREWORN():
	def __init__(self,): 
		self.name = "CAREWORN"
		self.definitions = [u'appearing tired, worried, and unhappy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
