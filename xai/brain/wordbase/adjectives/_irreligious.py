

#calss header
class _IRRELIGIOUS():
	def __init__(self,): 
		self.name = "IRRELIGIOUS"
		self.definitions = [u'having no interest in religion, or generally opposed to religion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
