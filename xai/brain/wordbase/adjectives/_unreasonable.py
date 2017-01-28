

#calss header
class _UNREASONABLE():
	def __init__(self,): 
		self.name = "UNREASONABLE"
		self.definitions = [u'not fair or acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
