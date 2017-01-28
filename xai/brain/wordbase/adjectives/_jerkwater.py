

#calss header
class _JERKWATER():
	def __init__(self,): 
		self.name = "JERKWATER"
		self.definitions = [u'used to describe a place that is small, not important, and a long way from other places: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
