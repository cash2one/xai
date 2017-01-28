

#calss header
class _WARMING():
	def __init__(self,): 
		self.name = "WARMING"
		self.definitions = [u'A warming type of food or drink makes you feel warm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
