

#calss header
class _INEBRIATED():
	def __init__(self,): 
		self.name = "INEBRIATED"
		self.definitions = [u'having drunk too much alcohol: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
