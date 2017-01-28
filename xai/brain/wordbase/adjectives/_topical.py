

#calss header
class _TOPICAL():
	def __init__(self,): 
		self.name = "TOPICAL"
		self.definitions = [u'of interest at the present time; relating to things that are happening at present: ', u'A topical medical product is used on the outside of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
