

#calss header
class _LIVELY():
	def __init__(self,): 
		self.name = "LIVELY"
		self.definitions = [u'full of energy and enthusiasm; interesting and exciting : ', u'(of colours) bright and strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
