

#calss header
class _IRRESPECTIVE():
	def __init__(self,): 
		self.name = "IRRESPECTIVE"
		self.definitions = [u'without considering; not needing to allow for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
