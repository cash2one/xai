

#calss header
class _UNUSED():
	def __init__(self,): 
		self.name = "UNUSED"
		self.definitions = [u'not being used at present, or never having been used: ', u'to not be familiar with a particular habit or experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
