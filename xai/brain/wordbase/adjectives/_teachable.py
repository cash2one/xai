

#calss header
class _TEACHABLE():
	def __init__(self,): 
		self.name = "TEACHABLE"
		self.definitions = [u'able to be taught; that can be taught: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
