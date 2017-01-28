

#calss header
class _ELITIST():
	def __init__(self,): 
		self.name = "ELITIST"
		self.definitions = [u'organized for the good of a few people who have special interests or abilities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
