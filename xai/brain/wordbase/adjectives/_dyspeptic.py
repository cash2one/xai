

#calss header
class _DYSPEPTIC():
	def __init__(self,): 
		self.name = "DYSPEPTIC"
		self.definitions = [u'having problems with digesting food', u'always angry or easily annoyed']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
