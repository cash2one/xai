

#calss header
class _GLANDULAR():
	def __init__(self,): 
		self.name = "GLANDULAR"
		self.definitions = [u'belonging or relating to, or produced or caused by, a gland or glands: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
