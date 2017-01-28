

#calss header
class _UNUSABLE():
	def __init__(self,): 
		self.name = "UNUSABLE"
		self.definitions = [u'Something that is unusable cannot be used, especially because it is broken or not safe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
