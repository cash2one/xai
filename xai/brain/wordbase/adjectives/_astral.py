

#calss header
class _ASTRAL():
	def __init__(self,): 
		self.name = "ASTRAL"
		self.definitions = [u'relating to the stars or outer space', u'relating to forces that are not known or understood']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
