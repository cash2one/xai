

#calss header
class _FUNCTIONALLY():
	def __init__(self,): 
		self.name = "FUNCTIONALLY"
		self.definitions = [u'in a way that is practical and useful rather than attractive: ', u'in a way that works normally']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
