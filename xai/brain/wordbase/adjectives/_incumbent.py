

#calss header
class _INCUMBENT():
	def __init__(self,): 
		self.name = "INCUMBENT"
		self.definitions = [u'officially having the named position: ', u'to be necessary for someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
