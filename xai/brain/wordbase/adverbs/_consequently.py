

#calss header
class _CONSEQUENTLY():
	def __init__(self,): 
		self.name = "CONSEQUENTLY"
		self.definitions = [u'as a result: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
