

#calss header
class _SECLUSIVE():
	def __init__(self,): 
		self.name = "SECLUSIVE"
		self.definitions = [u'preferring to be alone, away from other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
