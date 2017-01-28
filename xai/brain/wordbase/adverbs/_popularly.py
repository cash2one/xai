

#calss header
class _POPULARLY():
	def __init__(self,): 
		self.name = "POPULARLY"
		self.definitions = [u'by many people, especially by ordinary people rather than experts: ', u'A popularly elected person or government has been elected in a democratic election: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
