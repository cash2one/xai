

#calss header
class _TRUE():
	def __init__(self,): 
		self.name = "TRUE"
		self.definitions = [u'straight and without moving to either side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
