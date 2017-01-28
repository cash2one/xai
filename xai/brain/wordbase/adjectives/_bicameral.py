

#calss header
class _BICAMERAL():
	def __init__(self,): 
		self.name = "BICAMERAL"
		self.definitions = [u'(of a parliament, congress, etc.) having two parts, such as the Senate and the House of Representatives in the US']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
