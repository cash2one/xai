

#calss header
class _FATTENING():
	def __init__(self,): 
		self.name = "FATTENING"
		self.definitions = [u'Fattening food contains a lot of fat, sugar, etc. that would quickly make you fatter if you ate a lot of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
