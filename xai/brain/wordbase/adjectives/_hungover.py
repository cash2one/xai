

#calss header
class _HUNGOVER():
	def __init__(self,): 
		self.name = "HUNGOVER"
		self.definitions = [u'feeling ill with a bad pain in the head and often wanting to vomit after having drunk too much alcohol: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
