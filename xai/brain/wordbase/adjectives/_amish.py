

#calss header
class _AMISH():
	def __init__(self,): 
		self.name = "AMISH"
		self.definitions = [u'of or relating to the Amish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
