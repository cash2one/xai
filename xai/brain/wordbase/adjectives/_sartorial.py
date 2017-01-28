

#calss header
class _SARTORIAL():
	def __init__(self,): 
		self.name = "SARTORIAL"
		self.definitions = [u"relating to the making of clothes, usually men's clothes, or to a way of dressing: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
