

#calss header
class _TRANSITIONAL():
	def __init__(self,): 
		self.name = "TRANSITIONAL"
		self.definitions = [u'belonging or relating to a change, or the process of change, from one form or type to another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
