

#calss header
class _VARIOUSLY():
	def __init__(self,): 
		self.name = "VARIOUSLY"
		self.definitions = [u'in several different ways, at several different times, or by several different people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
