

#calss header
class _HALLOWED():
	def __init__(self,): 
		self.name = "HALLOWED"
		self.definitions = [u'very respected and praised because of great importance or great age: ', u'holy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
