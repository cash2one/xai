

#calss header
class _CONTINENT():
	def __init__(self,): 
		self.name = "CONTINENT"
		self.definitions = [u'able to control when you urinate and empty your bowels', u'able to control your sexual desires']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
