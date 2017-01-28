

#calss header
class _MAGNETIC():
	def __init__(self,): 
		self.name = "MAGNETIC"
		self.definitions = [u'with the power of a magnet', u'used to describe someone whose personality attracts a lot of people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
