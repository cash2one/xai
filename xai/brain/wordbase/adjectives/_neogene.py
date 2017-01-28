

#calss header
class _NEOGENE():
	def __init__(self,): 
		self.name = "NEOGENE"
		self.definitions = [u'from or referring to the period of time between about 22 and 2.5 million years ago, in which many modern mammals and the earliest forms of humans appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
