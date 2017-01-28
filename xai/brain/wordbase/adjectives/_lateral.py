

#calss header
class _LATERAL():
	def __init__(self,): 
		self.name = "LATERAL"
		self.definitions = [u'relating to the sides of an object or plant or to sideways movement: ', u'A lateral consonant is made when the flow of air is blocked in the middle, so that the air flows to the side: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
