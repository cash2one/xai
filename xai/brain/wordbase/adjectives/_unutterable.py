

#calss header
class _UNUTTERABLE():
	def __init__(self,): 
		self.name = "UNUTTERABLE"
		self.definitions = [u'too bad to be expressed in words; extreme: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
