

#calss header
class _PERVERTED():
	def __init__(self,): 
		self.name = "PERVERTED"
		self.definitions = [u'considered strange and unpleasant by most people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
