

#calss header
class _HYGIENIC():
	def __init__(self,): 
		self.name = "HYGIENIC"
		self.definitions = [u'clean, especially in order to prevent disease: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
