

#calss header
class _GINGER():
	def __init__(self,): 
		self.name = "GINGER"
		self.definitions = [u'having a red or orange-brown colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
