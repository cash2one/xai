

#calss header
class _POPULIST():
	def __init__(self,): 
		self.name = "POPULIST"
		self.definitions = [u'representing or relating to the ideas and opinions of ordinary people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
