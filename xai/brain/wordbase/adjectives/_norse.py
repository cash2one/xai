

#calss header
class _NORSE():
	def __init__(self,): 
		self.name = "NORSE"
		self.definitions = [u'belonging or relating to the people who lived in Scandinavia in the past, especially the Vikings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
