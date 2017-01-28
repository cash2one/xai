

#calss header
class _ENGLISH():
	def __init__(self,): 
		self.name = "ENGLISH"
		self.definitions = [u'in or relating to the English language: ', u'relating to or from England: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
