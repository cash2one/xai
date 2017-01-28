

#calss header
class _CODED():
	def __init__(self,): 
		self.name = "CODED"
		self.definitions = [u'written or sent in code: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
