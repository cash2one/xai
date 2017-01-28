

#calss header
class _PICT():
	def __init__(self,): 
		self.name = "PICT"
		self.definitions = [u'belonging or relating to the Picts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
