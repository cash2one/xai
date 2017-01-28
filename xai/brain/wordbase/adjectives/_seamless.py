

#calss header
class _SEAMLESS():
	def __init__(self,): 
		self.name = "SEAMLESS"
		self.definitions = [u'without any seams (= lines of sewing joining different pieces of cloth): ', u'happening without any sudden changes, interruption, or difficulty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
