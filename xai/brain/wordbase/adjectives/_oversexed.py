

#calss header
class _OVERSEXED():
	def __init__(self,): 
		self.name = "OVERSEXED"
		self.definitions = [u'wanting sex more often than is considered normal']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
