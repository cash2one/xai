

#calss header
class _MARAUDING():
	def __init__(self,): 
		self.name = "MARAUDING"
		self.definitions = [u'going from one place to another killing or using violence, stealing, and destroying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
