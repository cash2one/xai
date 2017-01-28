

#calss header
class _DENSE():
	def __init__(self,): 
		self.name = "DENSE"
		self.definitions = [u'having parts that are close together so that it is difficult to go or see through: ', u'stupid: ', u'(of a substance) containing a lot of matter in a small space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
