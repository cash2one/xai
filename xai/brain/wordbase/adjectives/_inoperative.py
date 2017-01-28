

#calss header
class _INOPERATIVE():
	def __init__(self,): 
		self.name = "INOPERATIVE"
		self.definitions = [u'(of a law, rule, etc.) not having effect or power, or (of a machine, system, etc.) not working or not able to work as usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
