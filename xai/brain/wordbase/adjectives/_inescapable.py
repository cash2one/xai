

#calss header
class _INESCAPABLE():
	def __init__(self,): 
		self.name = "INESCAPABLE"
		self.definitions = [u'If a fact or a situation is inescapable, it cannot be ignored or avoided.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
