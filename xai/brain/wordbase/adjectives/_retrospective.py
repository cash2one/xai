

#calss header
class _RETROSPECTIVE():
	def __init__(self,): 
		self.name = "RETROSPECTIVE"
		self.definitions = [u'relating to or thinking about the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
