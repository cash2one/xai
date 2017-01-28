

#calss header
class _DIVINE():
	def __init__(self,): 
		self.name = "DIVINE"
		self.definitions = [u'connected with a god, or like a god: ', u'extremely good, pleasant, or enjoyable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
