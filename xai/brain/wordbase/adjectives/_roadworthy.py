

#calss header
class _ROADWORTHY():
	def __init__(self,): 
		self.name = "ROADWORTHY"
		self.definitions = [u'(of a vehicle) in good enough condition to be driven without danger']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
