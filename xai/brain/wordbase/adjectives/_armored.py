

#calss header
class _ARMORED():
	def __init__(self,): 
		self.name = "ARMORED"
		self.definitions = [u'US spelling of  armoured ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
