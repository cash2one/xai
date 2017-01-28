

#calss header
class _HAD():
	def __init__(self,): 
		self.name = "HAD"
		self.definitions = [u'to be tricked and given less than you agreed or paid for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
