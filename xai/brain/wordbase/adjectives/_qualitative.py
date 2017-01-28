

#calss header
class _QUALITATIVE():
	def __init__(self,): 
		self.name = "QUALITATIVE"
		self.definitions = [u'relating to how good or bad something is: ', u'relating to what something or someone is like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
