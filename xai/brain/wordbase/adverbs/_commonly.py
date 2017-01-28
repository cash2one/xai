

#calss header
class _COMMONLY():
	def __init__(self,): 
		self.name = "COMMONLY"
		self.definitions = [u'often or usually: ', u'shared by two or more people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
