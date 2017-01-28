

#calss header
class _DIZZYING():
	def __init__(self,): 
		self.name = "DIZZYING"
		self.definitions = [u'causing you to feel dizzy: ', u'very fast or confusing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
