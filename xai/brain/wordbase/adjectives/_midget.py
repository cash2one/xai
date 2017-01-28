

#calss header
class _MIDGET():
	def __init__(self,): 
		self.name = "MIDGET"
		self.definitions = [u'used to describe an object that is much smaller than usual: ', u'Midget sports are organized competitions for children: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
