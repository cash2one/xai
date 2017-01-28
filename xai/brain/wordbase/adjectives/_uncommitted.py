

#calss header
class _UNCOMMITTED():
	def __init__(self,): 
		self.name = "UNCOMMITTED"
		self.definitions = [u'having made no promise to support any particular group, plan, belief, or action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
