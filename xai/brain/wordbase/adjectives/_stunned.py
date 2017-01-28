

#calss header
class _STUNNED():
	def __init__(self,): 
		self.name = "STUNNED"
		self.definitions = [u'very shocked or surprised: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
