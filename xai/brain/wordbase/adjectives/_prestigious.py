

#calss header
class _PRESTIGIOUS():
	def __init__(self,): 
		self.name = "PRESTIGIOUS"
		self.definitions = [u'very much respected and admired, usually because of being important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
