

#calss header
class _OVERWHELMINGLY():
	def __init__(self,): 
		self.name = "OVERWHELMINGLY"
		self.definitions = [u'strongly or completely; in an overwhelming way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
