

#calss header
class _HANDPICKED():
	def __init__(self,): 
		self.name = "HANDPICKED"
		self.definitions = [u'Someone who is handpicked has been carefully chosen for a special job or purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
