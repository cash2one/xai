

#calss header
class _NOTIONAL():
	def __init__(self,): 
		self.name = "NOTIONAL"
		self.definitions = [u'existing only as an idea, not as something real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
