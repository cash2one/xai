

#calss header
class _INSUPPORTABLE():
	def __init__(self,): 
		self.name = "INSUPPORTABLE"
		self.definitions = [u'difficult or impossible to bear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
