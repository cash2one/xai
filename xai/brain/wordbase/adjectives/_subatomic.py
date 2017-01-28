

#calss header
class _SUBATOMIC():
	def __init__(self,): 
		self.name = "SUBATOMIC"
		self.definitions = [u'smaller than or within an atom']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
