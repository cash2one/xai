

#calss header
class _JOINTED():
	def __init__(self,): 
		self.name = "JOINTED"
		self.definitions = [u'having joints and able to bend', u'having a place or places where two things are fastened together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
