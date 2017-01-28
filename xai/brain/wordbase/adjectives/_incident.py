

#calss header
class _INCIDENT():
	def __init__(self,): 
		self.name = "INCIDENT"
		self.definitions = [u'touching or hitting the surface of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
