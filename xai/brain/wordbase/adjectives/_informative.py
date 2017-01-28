

#calss header
class _INFORMATIVE():
	def __init__(self,): 
		self.name = "INFORMATIVE"
		self.definitions = [u'providing a lot of useful information: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
