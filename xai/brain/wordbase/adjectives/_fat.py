

#calss header
class _FAT():
	def __init__(self,): 
		self.name = "FAT"
		self.definitions = [u'having a lot of flesh on the body: ', u'thick or large: ', u'used in some phrases to mean very little or none: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
