

#calss header
class _LISSOME():
	def __init__(self,): 
		self.name = "LISSOME"
		self.definitions = [u'attractively thin and able to move quickly and smoothly']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
