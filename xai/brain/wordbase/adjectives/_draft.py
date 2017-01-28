

#calss header
class _DRAFT():
	def __init__(self,): 
		self.name = "DRAFT"
		self.definitions = [u'A draft plan, document, etc. is in its first form, including the main points but not all the details: ', u'(of drinks such as beer) stored in and served from large containers, especially barrels: ', u'(of animals) used for pulling heavy loads, vehicles, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
