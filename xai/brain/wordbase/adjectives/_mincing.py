

#calss header
class _MINCING():
	def __init__(self,): 
		self.name = "MINCING"
		self.definitions = [u'A mincing walk uses small, delicate steps in a way that does not look natural: ', u'used to describe a way of speaking that is too delicate and not direct enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
