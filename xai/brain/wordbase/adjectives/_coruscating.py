

#calss header
class _CORUSCATING():
	def __init__(self,): 
		self.name = "CORUSCATING"
		self.definitions = [u'flashing brightly', u'extremely intelligent and exciting or humorous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
