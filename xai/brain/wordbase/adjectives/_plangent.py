

#calss header
class _PLANGENT():
	def __init__(self,): 
		self.name = "PLANGENT"
		self.definitions = [u'(of sounds) deep, low, and expressing sadness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
