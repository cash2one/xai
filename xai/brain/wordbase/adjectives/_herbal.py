

#calss header
class _HERBAL():
	def __init__(self,): 
		self.name = "HERBAL"
		self.definitions = [u'relating to or made from herbs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
