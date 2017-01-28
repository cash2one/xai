

#calss header
class _OVERWHELMING():
	def __init__(self,): 
		self.name = "OVERWHELMING"
		self.definitions = [u'difficult to fight against: ', u'very great or very large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
