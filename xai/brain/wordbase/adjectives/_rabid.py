

#calss header
class _RABID():
	def __init__(self,): 
		self.name = "RABID"
		self.definitions = [u'suffering from rabies: ', u'having and expressing extreme and unreasonable feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
