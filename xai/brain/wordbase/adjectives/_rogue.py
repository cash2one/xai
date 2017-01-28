

#calss header
class _ROGUE():
	def __init__(self,): 
		self.name = "ROGUE"
		self.definitions = [u'behaving in ways that are not expected or not normal, often in a way that causes damage: ', u'A rogue animal is a dangerous wild animal that lives apart from the rest of its group.', u'to start behaving in a way that is not normal or expected, especially by leaving your group and doing something dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
