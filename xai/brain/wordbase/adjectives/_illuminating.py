

#calss header
class _ILLUMINATING():
	def __init__(self,): 
		self.name = "ILLUMINATING"
		self.definitions = [u'giving you new information about a subject or making it easier to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
