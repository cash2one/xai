

#calss header
class _CONTRARY():
	def __init__(self,): 
		self.name = "CONTRARY"
		self.definitions = [u'opposite: ', u'in a different way from what most people believe: ', u'A contrary person wants to disagree with and annoy other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
