

#calss header
class _SPOTTED():
	def __init__(self,): 
		self.name = "SPOTTED"
		self.definitions = [u'covered in small, usually round areas of colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
