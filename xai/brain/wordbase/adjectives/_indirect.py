

#calss header
class _INDIRECT():
	def __init__(self,): 
		self.name = "INDIRECT"
		self.definitions = [u'happening in addition to an intended result, often in a way that is complicated or not obvious: ', u'avoiding clearly mentioning or saying something: ', u'not following a straight line, or not directly or simply connected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
