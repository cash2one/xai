

#calss header
class _BITTERLY():
	def __init__(self,): 
		self.name = "BITTERLY"
		self.definitions = [u'in a way that shows strong negative emotion such as anger or disappointment: ', u'extremely and unpleasantly cold']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
