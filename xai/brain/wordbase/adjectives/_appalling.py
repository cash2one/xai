

#calss header
class _APPALLING():
	def __init__(self,): 
		self.name = "APPALLING"
		self.definitions = [u'very bad: ', u'shocking and very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
