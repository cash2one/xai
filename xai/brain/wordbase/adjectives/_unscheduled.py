

#calss header
class _UNSCHEDULED():
	def __init__(self,): 
		self.name = "UNSCHEDULED"
		self.definitions = [u'not planned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
