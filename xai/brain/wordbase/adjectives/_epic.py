

#calss header
class _EPIC():
	def __init__(self,): 
		self.name = "EPIC"
		self.definitions = [u'in the style of an epic: ', u'used to describe events that happen over a long period and involve a lot of action and difficulty: ', u'extremely large: ', u'extremely good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
