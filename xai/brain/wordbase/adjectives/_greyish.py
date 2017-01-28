

#calss header
class _GREYISH():
	def __init__(self,): 
		self.name = "GREYISH"
		self.definitions = [u'slightly grey in colour ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
