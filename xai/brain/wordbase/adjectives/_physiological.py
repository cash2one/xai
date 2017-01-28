

#calss header
class _PHYSIOLOGICAL():
	def __init__(self,): 
		self.name = "PHYSIOLOGICAL"
		self.definitions = [u'relating to the way in which the bodies of living things work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
