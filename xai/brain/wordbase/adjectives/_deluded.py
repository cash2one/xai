

#calss header
class _DELUDED():
	def __init__(self,): 
		self.name = "DELUDED"
		self.definitions = [u'believing things that are not real or true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
