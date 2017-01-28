

#calss header
class _FITTED():
	def __init__(self,): 
		self.name = "FITTED"
		self.definitions = [u'made to fit the shape of someone or something: ', u'permanently fixed in position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
