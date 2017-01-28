

#calss header
class _OSTENTATIOUS():
	def __init__(self,): 
		self.name = "OSTENTATIOUS"
		self.definitions = [u'too obviously showing your money, possessions, or power, in an attempt to make other people notice and admire you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
