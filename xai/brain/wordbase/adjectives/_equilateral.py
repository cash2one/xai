

#calss header
class _EQUILATERAL():
	def __init__(self,): 
		self.name = "EQUILATERAL"
		self.definitions = [u'used to describe a shape whose sides are all the same length: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
