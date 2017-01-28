

#calss header
class _JOINT():
	def __init__(self,): 
		self.name = "JOINT"
		self.definitions = [u'belonging to or shared between two or more people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
