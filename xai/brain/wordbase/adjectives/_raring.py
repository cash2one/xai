

#calss header
class _RARING():
	def __init__(self,): 
		self.name = "RARING"
		self.definitions = [u'to be very enthusiastic about starting something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
