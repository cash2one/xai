

#calss header
class _AMORAL():
	def __init__(self,): 
		self.name = "AMORAL"
		self.definitions = [u'without moral principles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
