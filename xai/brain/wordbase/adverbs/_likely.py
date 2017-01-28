

#calss header
class _LIKELY():
	def __init__(self,): 
		self.name = "LIKELY"
		self.definitions = [u'probably: ', u'probably: ', u'very probably: ', u'certainly not!: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
