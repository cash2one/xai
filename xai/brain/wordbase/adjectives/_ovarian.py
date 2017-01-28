

#calss header
class _OVARIAN():
	def __init__(self,): 
		self.name = "OVARIAN"
		self.definitions = [u'of or relating to the ovaries or an ovary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
