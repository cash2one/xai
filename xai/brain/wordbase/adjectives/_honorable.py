

#calss header
class _HONORABLE():
	def __init__(self,): 
		self.name = "HONORABLE"
		self.definitions = [u'US spelling of  honourable ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
