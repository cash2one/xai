

#calss header
class _FAVOURABLE():
	def __init__(self,): 
		self.name = "FAVOURABLE"
		self.definitions = [u'showing that you like or approve of someone or something: ', u'making you support or approve of someone or something: ', u'giving you an advantage or more chance of success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
