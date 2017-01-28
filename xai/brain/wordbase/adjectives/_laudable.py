

#calss header
class _LAUDABLE():
	def __init__(self,): 
		self.name = "LAUDABLE"
		self.definitions = [u'(of actions and behaviour) deserving praise, even if there is little or no success: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
