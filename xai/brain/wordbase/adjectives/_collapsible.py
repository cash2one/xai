

#calss header
class _COLLAPSIBLE():
	def __init__(self,): 
		self.name = "COLLAPSIBLE"
		self.definitions = [u'Collapsible furniture can be folded, usually so it can be put or stored in a smaller space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
