

#calss header
class _OBSCURE():
	def __init__(self,): 
		self.name = "OBSCURE"
		self.definitions = [u'not known to many people: ', u'not clear and difficult to understand or see: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
