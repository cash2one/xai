

#calss header
class _BELOW():
	def __init__(self,): 
		self.name = "BELOW"
		self.definitions = [u'in a lower position (than), under: ', u'less than a particular amount or level: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
