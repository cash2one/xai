

#calss header
class _PEREMPTORY():
	def __init__(self,): 
		self.name = "PEREMPTORY"
		self.definitions = [u'expecting to be obeyed immediately and without asking questions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
