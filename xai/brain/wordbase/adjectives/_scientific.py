

#calss header
class _SCIENTIFIC():
	def __init__(self,): 
		self.name = "SCIENTIFIC"
		self.definitions = [u'relating to science, or using the organized methods of science: ', u'careful and using a system or method: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
