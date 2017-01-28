

#calss header
class _MUTED():
	def __init__(self,): 
		self.name = "MUTED"
		self.definitions = [u'not loud: ', u'showing little enthusiasm: ', u'A muted colour is not bright: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
