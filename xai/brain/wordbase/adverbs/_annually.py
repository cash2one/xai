

#calss header
class _ANNUALLY():
	def __init__(self,): 
		self.name = "ANNUALLY"
		self.definitions = [u'once every year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
