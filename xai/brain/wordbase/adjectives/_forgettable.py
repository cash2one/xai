

#calss header
class _FORGETTABLE():
	def __init__(self,): 
		self.name = "FORGETTABLE"
		self.definitions = [u'not important or good enough to be remembered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
