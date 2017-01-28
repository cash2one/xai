

#calss header
class _SPENT():
	def __init__(self,): 
		self.name = "SPENT"
		self.definitions = [u'Something that is spent has been used so that it no longer has any power or effectiveness: ', u'tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
