

#calss header
class _REACHABLE():
	def __init__(self,): 
		self.name = "REACHABLE"
		self.definitions = [u'If a place is reachable, it is possible to get to it: ', u'If a level, especially a high one, is reachable, it is possible to get to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
