

#calss header
class _IMPOSSIBLY():
	def __init__(self,): 
		self.name = "IMPOSSIBLY"
		self.definitions = [u'extremely or more than is usual: ', u'in a way that cannot happen or be expected to happen']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
