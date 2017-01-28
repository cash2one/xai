

#calss header
class _PREDICATIVE():
	def __init__(self,): 
		self.name = "PREDICATIVE"
		self.definitions = [u'(in grammar, especially of adjectives or phrases) following a verb: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
