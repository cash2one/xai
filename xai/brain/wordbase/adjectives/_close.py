

#calss header
class _CLOSE():
	def __init__(self,): 
		self.name = "CLOSE"
		self.definitions = [u'not far in position or time: ', u'near: ', u'having only a small difference: ', u'almost: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
