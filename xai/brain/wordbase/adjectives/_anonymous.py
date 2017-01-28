

#calss header
class _ANONYMOUS():
	def __init__(self,): 
		self.name = "ANONYMOUS"
		self.definitions = [u'made or done by someone whose name is not known or not made public: ', u'having no unusual or interesting features: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
