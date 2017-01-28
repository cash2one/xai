

#calss header
class _NEEDLESSLY():
	def __init__(self,): 
		self.name = "NEEDLESSLY"
		self.definitions = [u'in a way that is not necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
