

#calss header
class _STRICTLY():
	def __init__(self,): 
		self.name = "STRICTLY"
		self.definitions = [u'in a way that would bring severe punishment if not obeyed: ', u'in a very limited or limiting way: ', u'exactly or correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
