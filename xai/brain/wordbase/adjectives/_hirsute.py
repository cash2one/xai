

#calss header
class _HIRSUTE():
	def __init__(self,): 
		self.name = "HIRSUTE"
		self.definitions = [u'having a lot of hair, especially on the face or body']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
