

#calss header
class _TENUOUS():
	def __init__(self,): 
		self.name = "TENUOUS"
		self.definitions = [u'A tenuous connection, idea, or situation is weak and possibly does not exist: ', u'thin, weak, and easily broken']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
