

#calss header
class _PUFFY():
	def __init__(self,): 
		self.name = "PUFFY"
		self.definitions = [u'If the skin around your eyes is puffy, it is slightly swollen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
