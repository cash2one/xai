

#calss header
class _BIPOLAR():
	def __init__(self,): 
		self.name = "BIPOLAR"
		self.definitions = [u'suffering from bipolar disorder']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
