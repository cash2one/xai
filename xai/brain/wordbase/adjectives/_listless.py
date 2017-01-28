

#calss header
class _LISTLESS():
	def __init__(self,): 
		self.name = "LISTLESS"
		self.definitions = [u'having no energy and enthusiasm and unwilling to do anything needing effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
