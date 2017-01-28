

#calss header
class _MAINSTREAM():
	def __init__(self,): 
		self.name = "MAINSTREAM"
		self.definitions = [u'considered normal, and having or using ideas, beliefs, etc. that are accepted by most people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
