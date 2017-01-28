

#calss header
class _MARTIAN():
	def __init__(self,): 
		self.name = "MARTIAN"
		self.definitions = [u'relating to the planet Mars, or to creatures that are believed to come from Mars : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
