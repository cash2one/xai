

#calss header
class _PLUNGING():
	def __init__(self,): 
		self.name = "PLUNGING"
		self.definitions = [u'dropping suddenly or having a shape that drops a long way down: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
