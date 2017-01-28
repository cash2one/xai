

#calss header
class _NONPLUSSED():
	def __init__(self,): 
		self.name = "NONPLUSSED"
		self.definitions = [u'surprised, confused, and not certain how to react: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
