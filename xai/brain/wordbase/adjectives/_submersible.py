

#calss header
class _SUBMERSIBLE():
	def __init__(self,): 
		self.name = "SUBMERSIBLE"
		self.definitions = [u'able to be used or to travel underwater: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
