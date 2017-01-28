

#calss header
class _PHILHARMONIC():
	def __init__(self,): 
		self.name = "PHILHARMONIC"
		self.definitions = [u'used in the names of musical groups, especially orchestras: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
