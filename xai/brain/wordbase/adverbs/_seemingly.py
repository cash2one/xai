

#calss header
class _SEEMINGLY():
	def __init__(self,): 
		self.name = "SEEMINGLY"
		self.definitions = [u'appearing to be something, especially when this is not true: ', u'according to the facts that you know: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
