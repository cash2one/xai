

#calss header
class _AWESTRUCK():
	def __init__(self,): 
		self.name = "AWESTRUCK"
		self.definitions = [u'filled with feelings of admiration or respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
