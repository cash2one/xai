

#calss header
class _UNCLAIMED():
	def __init__(self,): 
		self.name = "UNCLAIMED"
		self.definitions = [u'If something is unclaimed, no one has said that it belongs to them or that they should have it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
