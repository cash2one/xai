

#calss header
class _INADMISSIBLE():
	def __init__(self,): 
		self.name = "INADMISSIBLE"
		self.definitions = [u'unable to be accepted in a law court: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
