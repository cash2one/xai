

#calss header
class _ADMINISTRATIVE():
	def __init__(self,): 
		self.name = "ADMINISTRATIVE"
		self.definitions = [u'relating to the arrangements and work that is needed to control the operation of a plan or organization: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
