

#calss header
class _STRAPLESS():
	def __init__(self,): 
		self.name = "STRAPLESS"
		self.definitions = [u"A strapless dress, bra (= piece of underwear), or other piece of women's clothing does not have pieces of material going over the shoulders: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
