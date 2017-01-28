

#calss header
class _SEXIST():
	def __init__(self,): 
		self.name = "SEXIST"
		self.definitions = [u"Sexist jokes or remarks suggest that women are less able than men or refer to women's bodies, behaviour, or feelings in a negative way: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
