

#calss header
class _ARGUABLE():
	def __init__(self,): 
		self.name = "ARGUABLE"
		self.definitions = [u'If something is arguable, there could be some disagreement about it: ', u'it is possibly true that: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
