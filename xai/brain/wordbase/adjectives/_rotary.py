

#calss header
class _ROTARY():
	def __init__(self,): 
		self.name = "ROTARY"
		self.definitions = [u'(of a machine) having a part that moves around in a circle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
