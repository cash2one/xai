

#calss header
class _LOOSE():
	def __init__(self,): 
		self.name = "LOOSE"
		self.definitions = [u'not firmly held or fastened in place: ', u'Loose hair is not tied back: ', u'Loose things are not held together or attached to anything else: ', u'(of clothes) not fitting closely to the body: ', u'not tightly controlled, or not exact: ', u'having low morals; sexually free: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
