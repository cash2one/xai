

#calss header
class _METALLIC():
	def __init__(self,): 
		self.name = "METALLIC"
		self.definitions = [u'A metallic sound, appearance, or taste is like metal: ', u'consisting of, or partly consisting of, metal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
