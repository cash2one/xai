

#calss header
class _ABACK():
	def __init__(self,): 
		self.name = "ABACK"
		self.definitions = [u'to be very shocked or surprised: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
