

#calss header
class _ANTEBELLUM():
	def __init__(self,): 
		self.name = "ANTEBELLUM"
		self.definitions = [u'relating to the time before a war, especially the American Civil War: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
