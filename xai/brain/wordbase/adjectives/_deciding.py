

#calss header
class _DECIDING():
	def __init__(self,): 
		self.name = "DECIDING"
		self.definitions = [u'A deciding event or action is more important than the rest because the final result, decision, or choice is changed by it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
