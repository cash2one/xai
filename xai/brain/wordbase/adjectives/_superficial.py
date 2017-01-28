

#calss header
class _SUPERFICIAL():
	def __init__(self,): 
		self.name = "SUPERFICIAL"
		self.definitions = [u'(of a person) never thinking about things that are serious or important: ', u'not complete and involving only the most obvious things: ', u'appearing to be real or important when this is not true or correct: ', u'only on the surface of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
