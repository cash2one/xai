

#calss header
class _ROSY():
	def __init__(self,): 
		self.name = "ROSY"
		self.definitions = [u'having a colour between pink and red: ', u'If a situation is described as rosy, it gives hope of success or happiness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
