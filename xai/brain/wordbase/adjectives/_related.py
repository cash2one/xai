

#calss header
class _RELATED():
	def __init__(self,): 
		self.name = "RELATED"
		self.definitions = [u'connected: ', u'If people are related, they belong to the same family: ', u'If different types of animal are related, they come from the same type of animal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
