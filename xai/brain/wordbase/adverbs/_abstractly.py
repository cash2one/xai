

#calss header
class _ABSTRACTLY():
	def __init__(self,): 
		self.name = "ABSTRACTLY"
		self.definitions = [u'in a general way and not based on particular examples: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
