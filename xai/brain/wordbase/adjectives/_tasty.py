

#calss header
class _TASTY():
	def __init__(self,): 
		self.name = "TASTY"
		self.definitions = [u'Tasty food has a strong and very pleasant flavour: ', u'used to describe someone who is very sexually attractive']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
