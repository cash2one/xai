

#calss header
class _RUBBISH():
	def __init__(self,): 
		self.name = "RUBBISH"
		self.definitions = [u'completely without skill at a particular activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
