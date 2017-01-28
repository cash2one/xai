

#calss header
class _UNCONSCIOUS():
	def __init__(self,): 
		self.name = "UNCONSCIOUS"
		self.definitions = [u'in the state of not being awake, especially as the result of a head injury: ', u'An unconscious thought or feeling is one that you do not know you have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
