

#calss header
class _WILDLY():
	def __init__(self,): 
		self.name = "WILDLY"
		self.definitions = [u'in an uncontrolled or extreme way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
