

#calss header
class _USEFUL():
	def __init__(self,): 
		self.name = "USEFUL"
		self.definitions = [u'effective; helping you to do or achieve something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
