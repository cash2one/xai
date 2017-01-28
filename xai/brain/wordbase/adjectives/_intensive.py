

#calss header
class _INTENSIVE():
	def __init__(self,): 
		self.name = "INTENSIVE"
		self.definitions = [u'involving a lot of effort or activity in a short period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
