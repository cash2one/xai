

#calss header
class _CEPHALIC():
	def __init__(self,): 
		self.name = "CEPHALIC"
		self.definitions = [u'relating to the head: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
