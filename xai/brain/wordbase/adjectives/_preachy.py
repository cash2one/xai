

#calss header
class _PREACHY():
	def __init__(self,): 
		self.name = "PREACHY"
		self.definitions = [u'sounding as if you want to give someone moral advice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
