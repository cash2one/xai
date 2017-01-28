

#calss header
class _DISRUPTIVE():
	def __init__(self,): 
		self.name = "DISRUPTIVE"
		self.definitions = [u'causing trouble and therefore stopping something from continuing as usual: ', u'changing the traditional way that an industry operates, especially in a new and effective way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
