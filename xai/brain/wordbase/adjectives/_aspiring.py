

#calss header
class _ASPIRING():
	def __init__(self,): 
		self.name = "ASPIRING"
		self.definitions = [u'someone who is trying to become a successful actor, politician, writer, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
