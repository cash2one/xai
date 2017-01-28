

#calss header
class _BRUISED():
	def __init__(self,): 
		self.name = "BRUISED"
		self.definitions = [u'having bruises: ', u'emotionally hurt as a result of a bad experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
