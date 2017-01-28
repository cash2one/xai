

#calss header
class _TENSILE():
	def __init__(self,): 
		self.name = "TENSILE"
		self.definitions = [u'If a material is tensile, it can be stretched.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
