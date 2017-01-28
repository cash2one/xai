

#calss header
class _SKILLFULLY():
	def __init__(self,): 
		self.name = "SKILLFULLY"
		self.definitions = [u'US spelling of  skilfully ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
