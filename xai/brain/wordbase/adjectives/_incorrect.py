

#calss header
class _INCORRECT():
	def __init__(self,): 
		self.name = "INCORRECT"
		self.definitions = [u'not correct or not true: ', u'not acceptable or not as it should be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
