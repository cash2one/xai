

#calss header
class _ENVIOUS():
	def __init__(self,): 
		self.name = "ENVIOUS"
		self.definitions = [u'wishing you had what another person has: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
