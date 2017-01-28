

#calss header
class _RHEUMATIC():
	def __init__(self,): 
		self.name = "RHEUMATIC"
		self.definitions = [u'relating to inflammation of muscles, joints, heart valves, or other parts of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
