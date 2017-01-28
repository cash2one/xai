

#calss header
class _SAVAGELY():
	def __init__(self,): 
		self.name = "SAVAGELY"
		self.definitions = [u'in a violent, cruel, or very severe way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
