

#calss header
class _INVENTIVE():
	def __init__(self,): 
		self.name = "INVENTIVE"
		self.definitions = [u'very good at thinking of new and original ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
