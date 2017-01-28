

#calss header
class _CAPACIOUS():
	def __init__(self,): 
		self.name = "CAPACIOUS"
		self.definitions = [u'having a lot of space and able to contain a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
