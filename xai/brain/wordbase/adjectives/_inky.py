

#calss header
class _INKY():
	def __init__(self,): 
		self.name = "INKY"
		self.definitions = [u'covered with ink: ', u'very dark: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
