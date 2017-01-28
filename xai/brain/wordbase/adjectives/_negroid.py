

#calss header
class _NEGROID():
	def __init__(self,): 
		self.name = "NEGROID"
		self.definitions = [u'having the physical features of a black person from Africa']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
