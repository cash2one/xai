

#calss header
class _ACHY():
	def __init__(self,): 
		self.name = "ACHY"
		self.definitions = [u'Someone who feels achy has continuous pains in their body that are unpleasant but not very strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
