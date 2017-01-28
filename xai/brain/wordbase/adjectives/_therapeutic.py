

#calss header
class _THERAPEUTIC():
	def __init__(self,): 
		self.name = "THERAPEUTIC"
		self.definitions = [u'causing someone to feel happier and more relaxed or to be more healthy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
