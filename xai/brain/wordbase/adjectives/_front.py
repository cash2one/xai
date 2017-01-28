

#calss header
class _FRONT():
	def __init__(self,): 
		self.name = "FRONT"
		self.definitions = [u'in or at the front of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
