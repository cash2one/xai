

#calss header
class _THOROUGHLY():
	def __init__(self,): 
		self.name = "THOROUGHLY"
		self.definitions = [u'completely, very much: ', u'in a detailed and careful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
