

#calss header
class _ALRIGHT():
	def __init__(self,): 
		self.name = "ALRIGHT"
		self.definitions = [u'non-standard form of  all right ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
