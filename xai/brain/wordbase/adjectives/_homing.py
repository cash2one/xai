

#calss header
class _HOMING():
	def __init__(self,): 
		self.name = "HOMING"
		self.definitions = [u'relating to the ability of some animals to find their way home: ', u'(of an electronic device) producing a special signal so that it can be found using electronic equipment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
