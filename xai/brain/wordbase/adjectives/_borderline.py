

#calss header
class _BORDERLINE():
	def __init__(self,): 
		self.name = "BORDERLINE"
		self.definitions = [u'between two different conditions, with the possibility of belonging to either one of them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
