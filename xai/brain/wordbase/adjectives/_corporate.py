

#calss header
class _CORPORATE():
	def __init__(self,): 
		self.name = "CORPORATE"
		self.definitions = [u'relating to a large company: ', u'of or shared by a whole group and not just of a single member: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
