

#calss header
class _FRENZIED():
	def __init__(self,): 
		self.name = "FRENZIED"
		self.definitions = [u'uncontrolled and excited, sometimes violent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
