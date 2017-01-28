

#calss header
class _SKETCHY():
	def __init__(self,): 
		self.name = "SKETCHY"
		self.definitions = [u'containing few details: ', u'not completely safe or not completely honest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
