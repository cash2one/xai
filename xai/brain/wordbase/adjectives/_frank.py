

#calss header
class _FRANK():
	def __init__(self,): 
		self.name = "FRANK"
		self.definitions = [u'honest, sincere, and telling the truth, even when this might be awkward or make other people uncomfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
