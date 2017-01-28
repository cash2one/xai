

#calss header
class _DORKY():
	def __init__(self,): 
		self.name = "DORKY"
		self.definitions = [u'stupid and awkward: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
