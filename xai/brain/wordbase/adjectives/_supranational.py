

#calss header
class _SUPRANATIONAL():
	def __init__(self,): 
		self.name = "SUPRANATIONAL"
		self.definitions = [u'involving more than one country, or having power or authority that is greater than that of single countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
