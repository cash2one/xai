

#calss header
class _WORSE():
	def __init__(self,): 
		self.name = "WORSE"
		self.definitions = [u'comparative of  badly : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
