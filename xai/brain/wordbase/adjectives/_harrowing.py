

#calss header
class _HARROWING():
	def __init__(self,): 
		self.name = "HARROWING"
		self.definitions = [u'extremely upsetting because connected with suffering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
