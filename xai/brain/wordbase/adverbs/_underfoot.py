

#calss header
class _UNDERFOOT():
	def __init__(self,): 
		self.name = "UNDERFOOT"
		self.definitions = [u'under your feet as you walk; on the ground: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
