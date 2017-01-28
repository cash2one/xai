

#calss header
class _SCALENE():
	def __init__(self,): 
		self.name = "SCALENE"
		self.definitions = [u'relating to uneven, three sided body parts', u'relating to the scalenus muscles of the neck']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
