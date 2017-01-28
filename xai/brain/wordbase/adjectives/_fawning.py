

#calss header
class _FAWNING():
	def __init__(self,): 
		self.name = "FAWNING"
		self.definitions = [u'praising someone too much and giving them a lot of attention that is not sincere in order to get a positive reaction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
