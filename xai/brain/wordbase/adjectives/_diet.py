

#calss header
class _DIET():
	def __init__(self,): 
		self.name = "DIET"
		self.definitions = [u'Diet food or drink contains less sugar or fat than the usual type, and often contains an artificial sweetener: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
