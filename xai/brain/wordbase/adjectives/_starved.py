

#calss header
class _STARVED():
	def __init__(self,): 
		self.name = "STARVED"
		self.definitions = [u'very hungry', u'dangerously thin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
