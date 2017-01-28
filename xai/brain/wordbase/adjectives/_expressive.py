

#calss header
class _EXPRESSIVE():
	def __init__(self,): 
		self.name = "EXPRESSIVE"
		self.definitions = [u'showing what someone thinks or feels: ', u'showing a particular feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
