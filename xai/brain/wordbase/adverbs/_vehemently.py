

#calss header
class _VEHEMENTLY():
	def __init__(self,): 
		self.name = "VEHEMENTLY"
		self.definitions = [u'in a strong and emotional way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
