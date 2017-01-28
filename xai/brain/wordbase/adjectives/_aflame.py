

#calss header
class _AFLAME():
	def __init__(self,): 
		self.name = "AFLAME"
		self.definitions = [u'burning: ', u'red or gold, as if burning: ', u'very excited: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
