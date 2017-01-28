

#calss header
class _WEBBED():
	def __init__(self,): 
		self.name = "WEBBED"
		self.definitions = [u'If a bird or animal has webbed feet, its toes are connected by skin to help it when swimming: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
