

#calss header
class _CATHOLIC():
	def __init__(self,): 
		self.name = "CATHOLIC"
		self.definitions = [u'including many different types of thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
