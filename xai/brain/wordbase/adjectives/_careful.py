

#calss header
class _CAREFUL():
	def __init__(self,): 
		self.name = "CAREFUL"
		self.definitions = [u'giving a lot of attention to what you are doing so that you do not have an accident, make a mistake, or damage something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
