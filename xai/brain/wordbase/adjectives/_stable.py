

#calss header
class _STABLE():
	def __init__(self,): 
		self.name = "STABLE"
		self.definitions = [u'firmly fixed or not likely to move or change: ', u'A stable person is mentally healthy: ', u'A stable substance keeps the same chemical or atomic state.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
