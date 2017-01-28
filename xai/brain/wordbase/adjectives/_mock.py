

#calss header
class _MOCK():
	def __init__(self,): 
		self.name = "MOCK"
		self.definitions = [u'not real but appearing or pretending to be exactly like something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
