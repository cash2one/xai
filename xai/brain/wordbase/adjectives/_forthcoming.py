

#calss header
class _FORTHCOMING():
	def __init__(self,): 
		self.name = "FORTHCOMING"
		self.definitions = [u'happening soon: ', u'friendly and helpful, willing to give information or to talk: ', u'produced, supplied, or given: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
