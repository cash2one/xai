

#calss header
class _ROMANESQUE():
	def __init__(self,): 
		self.name = "ROMANESQUE"
		self.definitions = [u'relating to the style of building that was common in western and southern Europe from the 10th to the 12th centuries']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
