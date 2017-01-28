

#calss header
class _SPECIFICALLY():
	def __init__(self,): 
		self.name = "SPECIFICALLY"
		self.definitions = [u'for a particular reason, purpose, etc.: ', u'clearly, exactly, or in detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
