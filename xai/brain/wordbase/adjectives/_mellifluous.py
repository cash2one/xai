

#calss header
class _MELLIFLUOUS():
	def __init__(self,): 
		self.name = "MELLIFLUOUS"
		self.definitions = [u'having a pleasant and flowing sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
