

#calss header
class _DISENGAGED():
	def __init__(self,): 
		self.name = "DISENGAGED"
		self.definitions = [u'not feeling interested or involved in something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
