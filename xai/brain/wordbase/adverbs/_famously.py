

#calss header
class _FAMOUSLY():
	def __init__(self,): 
		self.name = "FAMOUSLY"
		self.definitions = [u'in a way that is famous or well known: ', u'extremely well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
