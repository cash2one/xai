

#calss header
class _SHAPELY():
	def __init__(self,): 
		self.name = "SHAPELY"
		self.definitions = [u"used to describe something that has an attractive form, especially a woman's body or parts of a woman's body: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
