

#calss header
class _THIN():
	def __init__(self,): 
		self.name = "THIN"
		self.definitions = [u'having a small distance between two opposite sides: ', u'(of the body) with little flesh on the bones: ', u'to be very thin: ', u'not difficult to see through: ', u'having only a small number of people or a small amount of something: ', u'(of a liquid) flowing easily: ', u'weak or of poor quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
