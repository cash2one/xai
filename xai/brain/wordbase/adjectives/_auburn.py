

#calss header
class _AUBURN():
	def __init__(self,): 
		self.name = "AUBURN"
		self.definitions = [u'(of hair) reddish-brown in colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
