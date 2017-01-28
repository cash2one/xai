

#calss header
class _SUBSERVIENT():
	def __init__(self,): 
		self.name = "SUBSERVIENT"
		self.definitions = [u'willing to do what other people want, or considering your wishes as less important than those of other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
