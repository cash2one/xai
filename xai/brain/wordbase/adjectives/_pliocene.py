

#calss header
class _PLIOCENE():
	def __init__(self,): 
		self.name = "PLIOCENE"
		self.definitions = [u'from or referring to the period of time between around 5.3 million and 1.8 million years ago, in which many modern mammals and the first modern humans appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
