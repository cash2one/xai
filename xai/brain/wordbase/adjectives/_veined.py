

#calss header
class _VEINED():
	def __init__(self,): 
		self.name = "VEINED"
		self.definitions = [u'with many veins, or covered with lines that look like veins: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
