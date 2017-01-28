

#calss header
class _UNPROMISING():
	def __init__(self,): 
		self.name = "UNPROMISING"
		self.definitions = [u'Something that is unpromising does not show any signs that it will be enjoyable or successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
