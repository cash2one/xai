

#calss header
class _THERMAL():
	def __init__(self,): 
		self.name = "THERMAL"
		self.definitions = [u'connected with heat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
