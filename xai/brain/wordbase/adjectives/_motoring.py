

#calss header
class _MOTORING():
	def __init__(self,): 
		self.name = "MOTORING"
		self.definitions = [u'relating to driving: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
