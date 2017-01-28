

#calss header
class _TRANSVERSE():
	def __init__(self,): 
		self.name = "TRANSVERSE"
		self.definitions = [u'in a position or direction that is at an angle of 90\xb0 to something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
