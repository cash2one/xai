

#calss header
class _FARMHOUSE():
	def __init__(self,): 
		self.name = "FARMHOUSE"
		self.definitions = [u'Farmhouse food is made using traditional methods: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
