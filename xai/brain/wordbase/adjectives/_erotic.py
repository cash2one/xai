

#calss header
class _EROTIC():
	def __init__(self,): 
		self.name = "EROTIC"
		self.definitions = [u'relating to sexual desire and pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
