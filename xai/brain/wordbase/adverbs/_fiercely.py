

#calss header
class _FIERCELY():
	def __init__(self,): 
		self.name = "FIERCELY"
		self.definitions = [u'in a frightening, violent, or powerful way: ', u'extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
