

#calss header
class _WARLIKE():
	def __init__(self,): 
		self.name = "WARLIKE"
		self.definitions = [u'often involved in and eager to start wars: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
