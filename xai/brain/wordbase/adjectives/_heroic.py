

#calss header
class _HEROIC():
	def __init__(self,): 
		self.name = "HEROIC"
		self.definitions = [u'very brave or great: ', u'If you make a heroic attempt or effort to do something, you try very hard to do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
