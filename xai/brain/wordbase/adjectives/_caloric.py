

#calss header
class _CALORIC():
	def __init__(self,): 
		self.name = "CALORIC"
		self.definitions = [u'relating to calories (= units of energy provided by food): ', u'containing a lot of calories: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
