

#calss header
class _LIGHTED():
	def __init__(self,): 
		self.name = "LIGHTED"
		self.definitions = [u'burning or starting to burn: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
