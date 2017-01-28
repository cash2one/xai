

#calss header
class _NEIGHBOURLY():
	def __init__(self,): 
		self.name = "NEIGHBOURLY"
		self.definitions = [u'friendly or helpful to your neighbours: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
