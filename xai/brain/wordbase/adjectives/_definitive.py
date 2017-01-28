

#calss header
class _DEFINITIVE():
	def __init__(self,): 
		self.name = "DEFINITIVE"
		self.definitions = [u'not able to be changed or improved: ', u'considered to be the best of its type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
