

#calss header
class _POSTWAR():
	def __init__(self,): 
		self.name = "POSTWAR"
		self.definitions = [u'happening or existing in the period after a war, especially the First or Second World War: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
