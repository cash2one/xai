

#calss header
class _CEREMONIOUS():
	def __init__(self,): 
		self.name = "CEREMONIOUS"
		self.definitions = [u'Ceremonious behaviour is very or too formal or polite.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
