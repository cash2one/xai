

#calss header
class _INTRAMURAL():
	def __init__(self,): 
		self.name = "INTRAMURAL"
		self.definitions = [u'happening within or involving the members of one school, college, or university: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
