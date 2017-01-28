

#calss header
class _ARTICULATE():
	def __init__(self,): 
		self.name = "ARTICULATE"
		self.definitions = [u'able to express thoughts and feelings easily and clearly, or showing this quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
