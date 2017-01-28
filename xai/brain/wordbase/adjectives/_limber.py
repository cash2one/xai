

#calss header
class _LIMBER():
	def __init__(self,): 
		self.name = "LIMBER"
		self.definitions = [u'(of a person) able to bend and move easily and smoothly']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
