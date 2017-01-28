

#calss header
class _COMEDIC():
	def __init__(self,): 
		self.name = "COMEDIC"
		self.definitions = [u'relating to or involving comedy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
