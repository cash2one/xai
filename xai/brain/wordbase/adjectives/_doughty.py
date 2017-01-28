

#calss header
class _DOUGHTY():
	def __init__(self,): 
		self.name = "DOUGHTY"
		self.definitions = [u'determined, brave, and unwilling ever to stop trying to achieve something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
