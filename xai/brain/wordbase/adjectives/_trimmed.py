

#calss header
class _TRIMMED():
	def __init__(self,): 
		self.name = "TRIMMED"
		self.definitions = [u'If clothes and other things made of cloth are trimmed, they are decorated, especially around the edges: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
