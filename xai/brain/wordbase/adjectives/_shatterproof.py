

#calss header
class _SHATTERPROOF():
	def __init__(self,): 
		self.name = "SHATTERPROOF"
		self.definitions = [u'Shatterproof glass or plastic, etc. is made so that it will not break into small pieces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
