

#calss header
class _OPPOSITE():
	def __init__(self,): 
		self.name = "OPPOSITE"
		self.definitions = [u'in a position facing someone or something but on the other side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
