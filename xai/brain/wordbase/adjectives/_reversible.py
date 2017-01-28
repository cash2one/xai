

#calss header
class _REVERSIBLE():
	def __init__(self,): 
		self.name = "REVERSIBLE"
		self.definitions = [u'If something is reversible, it can be changed back to what it was before: ', u'Reversible clothes can be worn so that the inside becomes the outside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
