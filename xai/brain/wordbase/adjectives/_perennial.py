

#calss header
class _PERENNIAL():
	def __init__(self,): 
		self.name = "PERENNIAL"
		self.definitions = [u'lasting a very long time, or happening repeatedly or all the time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
