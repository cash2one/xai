

#calss header
class _KINKY():
	def __init__(self,): 
		self.name = "KINKY"
		self.definitions = [u'unusual, strange, and possibly exciting, especially in ways involving unusual sexual acts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
