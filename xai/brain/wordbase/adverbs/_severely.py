

#calss header
class _SEVERELY():
	def __init__(self,): 
		self.name = "SEVERELY"
		self.definitions = [u'very seriously: ', u'in a way that is not kind or does not show sympathy: ', u'completely plainly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
