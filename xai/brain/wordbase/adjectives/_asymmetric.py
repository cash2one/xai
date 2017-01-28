

#calss header
class _ASYMMETRIC():
	def __init__(self,): 
		self.name = "ASYMMETRIC"
		self.definitions = [u'with two halves, sides, or parts that are not exactly the same in shape and size: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
