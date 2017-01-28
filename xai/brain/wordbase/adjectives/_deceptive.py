

#calss header
class _DECEPTIVE():
	def __init__(self,): 
		self.name = "DECEPTIVE"
		self.definitions = [u'making you believe something that is not true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
