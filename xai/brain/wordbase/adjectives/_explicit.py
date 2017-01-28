

#calss header
class _EXPLICIT():
	def __init__(self,): 
		self.name = "EXPLICIT"
		self.definitions = [u'clear and exact: ', u'showing or talking about sex or violence in a very detailed way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
