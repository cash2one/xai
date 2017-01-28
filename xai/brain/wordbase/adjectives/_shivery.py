

#calss header
class _SHIVERY():
	def __init__(self,): 
		self.name = "SHIVERY"
		self.definitions = [u'shaking slightly because you feel cold, frightened, or ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
