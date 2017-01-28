

#calss header
class _PULSATING():
	def __init__(self,): 
		self.name = "PULSATING"
		self.definitions = [u'very interesting and exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
