

#calss header
class _GRAYING():
	def __init__(self,): 
		self.name = "GRAYING"
		self.definitions = [u'US spelling of  greying ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
