

#calss header
class _INTRUSIVE():
	def __init__(self,): 
		self.name = "INTRUSIVE"
		self.definitions = [u'affecting someone in a way that annoys them and makes them feel uncomfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
