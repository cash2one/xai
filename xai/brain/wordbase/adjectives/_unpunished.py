

#calss header
class _UNPUNISHED():
	def __init__(self,): 
		self.name = "UNPUNISHED"
		self.definitions = [u'not punished: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
