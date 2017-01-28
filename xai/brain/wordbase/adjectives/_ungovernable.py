

#calss header
class _UNGOVERNABLE():
	def __init__(self,): 
		self.name = "UNGOVERNABLE"
		self.definitions = [u'unable to be governed or controlled']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
