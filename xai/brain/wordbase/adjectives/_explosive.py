

#calss header
class _EXPLOSIVE():
	def __init__(self,): 
		self.name = "EXPLOSIVE"
		self.definitions = [u'exploding or able to explode easily: ', u'very loud and sudden, like an explosion: ', u'An explosive situation or emotion is one in which strong feelings are loudly or violently expressed: ', u'An explosive increase is very large and quick: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
