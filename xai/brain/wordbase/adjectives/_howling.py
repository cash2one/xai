

#calss header
class _HOWLING():
	def __init__(self,): 
		self.name = "HOWLING"
		self.definitions = [u'to be very successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
