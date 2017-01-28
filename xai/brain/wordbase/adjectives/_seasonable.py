

#calss header
class _SEASONABLE():
	def __init__(self,): 
		self.name = "SEASONABLE"
		self.definitions = [u'expected at or suitable for a particular time of the year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
