

#calss header
class _UNGRATEFUL():
	def __init__(self,): 
		self.name = "UNGRATEFUL"
		self.definitions = [u'not showing or expressing any thanks']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
