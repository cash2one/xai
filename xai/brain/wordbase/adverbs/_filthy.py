

#calss header
class _FILTHY():
	def __init__(self,): 
		self.name = "FILTHY"
		self.definitions = [u'extremely dirty', u'extremely rich']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
