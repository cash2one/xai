

#calss header
class _HABITABLE():
	def __init__(self,): 
		self.name = "HABITABLE"
		self.definitions = [u'providing conditions that are good enough to live in or on: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
