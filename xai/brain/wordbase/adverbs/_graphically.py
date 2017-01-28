

#calss header
class _GRAPHICALLY():
	def __init__(self,): 
		self.name = "GRAPHICALLY"
		self.definitions = [u'in a very clear and powerful way: ', u'in a way that uses, consists of, or relates to graphs, or to drawing or printing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
