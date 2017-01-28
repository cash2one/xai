

#calss header
class _OPERATIVE():
	def __init__(self,): 
		self.name = "OPERATIVE"
		self.definitions = [u'working or being used: ', u'relating to a medical operation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
