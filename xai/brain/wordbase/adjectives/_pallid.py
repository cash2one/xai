

#calss header
class _PALLID():
	def __init__(self,): 
		self.name = "PALLID"
		self.definitions = [u'very pale, in a way that looks unhealthy and not attractive: ', u'showing no enthusiasm or excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
