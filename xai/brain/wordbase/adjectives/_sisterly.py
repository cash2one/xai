

#calss header
class _SISTERLY():
	def __init__(self,): 
		self.name = "SISTERLY"
		self.definitions = [u'feeling or behaving like a sister: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
