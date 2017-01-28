

#calss header
class _DEAR():
	def __init__(self,): 
		self.name = "DEAR"
		self.definitions = [u'loved or liked very much: ', u'used at the beginning of a letter to greet the person you are writing to: ', u'costing too much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
