

#calss header
class _THEMATIC():
	def __init__(self,): 
		self.name = "THEMATIC"
		self.definitions = [u'relating to or based on subjects or a theme: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
