

#calss header
class _BEWILDERING():
	def __init__(self,): 
		self.name = "BEWILDERING"
		self.definitions = [u'confusing and difficult to understand: ', u'making you feel confused because you cannot decide what you want: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
