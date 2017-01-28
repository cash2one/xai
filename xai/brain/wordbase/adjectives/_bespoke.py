

#calss header
class _BESPOKE():
	def __init__(self,): 
		self.name = "BESPOKE"
		self.definitions = [u'specially made for a particular person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
