

#calss header
class _ENIGMATIC():
	def __init__(self,): 
		self.name = "ENIGMATIC"
		self.definitions = [u'mysterious and impossible to understand completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
