

#calss header
class _EMOTIONAL():
	def __init__(self,): 
		self.name = "EMOTIONAL"
		self.definitions = [u'relating to the emotions: ', u'having and expressing strong feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
