

#calss header
class _YIDDISH():
	def __init__(self,): 
		self.name = "YIDDISH"
		self.definitions = [u'in or relating to Yiddish']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
