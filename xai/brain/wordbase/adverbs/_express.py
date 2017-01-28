

#calss header
class _EXPRESS():
	def __init__(self,): 
		self.name = "EXPRESS"
		self.definitions = [u'using a service that does something faster than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
