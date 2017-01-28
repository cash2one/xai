

#calss header
class _DOABLE():
	def __init__(self,): 
		self.name = "DOABLE"
		self.definitions = [u'If something is doable, it can be achieved or performed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
