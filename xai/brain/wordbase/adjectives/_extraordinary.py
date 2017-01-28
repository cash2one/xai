

#calss header
class _EXTRAORDINARY():
	def __init__(self,): 
		self.name = "EXTRAORDINARY"
		self.definitions = [u'very unusual, special, unexpected, or strange: ', u'a special meeting that happens between regular meetings']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
