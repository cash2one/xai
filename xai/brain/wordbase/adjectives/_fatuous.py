

#calss header
class _FATUOUS():
	def __init__(self,): 
		self.name = "FATUOUS"
		self.definitions = [u'stupid, not correct, or not carefully thought about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
