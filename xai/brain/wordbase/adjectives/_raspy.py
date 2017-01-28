

#calss header
class _RASPY():
	def __init__(self,): 
		self.name = "RASPY"
		self.definitions = [u'A raspy voice sounds unpleasantly rough.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
