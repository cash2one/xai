

#calss header
class _STRAIGHTFORWARD():
	def __init__(self,): 
		self.name = "STRAIGHTFORWARD"
		self.definitions = [u'easy to understand or simple: ', u'(of a person) honest and not likely to hide their opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
