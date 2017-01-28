

#calss header
class _UNEVENTFUL():
	def __init__(self,): 
		self.name = "UNEVENTFUL"
		self.definitions = [u'An uneventful time or situation is one in which nothing interesting or surprising happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
