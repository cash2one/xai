

#calss header
class _REQUISITE():
	def __init__(self,): 
		self.name = "REQUISITE"
		self.definitions = [u'necessary or needed for a particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
