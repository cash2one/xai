

#calss header
class _POTENTIALLY():
	def __init__(self,): 
		self.name = "POTENTIALLY"
		self.definitions = [u'possibly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
