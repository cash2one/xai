

#calss header
class _INAPT():
	def __init__(self,): 
		self.name = "INAPT"
		self.definitions = [u'not suitable for the situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
