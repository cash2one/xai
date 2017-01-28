

#calss header
class _COLLECT():
	def __init__(self,): 
		self.name = "COLLECT"
		self.definitions = [u'When you call collect or make a collect phone call, the person you call pays for the call: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
