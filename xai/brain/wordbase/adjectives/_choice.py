

#calss header
class _CHOICE():
	def __init__(self,): 
		self.name = "CHOICE"
		self.definitions = [u'of high quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
