

#calss header
class _MOTHERLY():
	def __init__(self,): 
		self.name = "MOTHERLY"
		self.definitions = [u'A motherly woman treats other people with a lot of kindness and love and tries to make certain they are happy.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
