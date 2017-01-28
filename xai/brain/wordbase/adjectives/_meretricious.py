

#calss header
class _MERETRICIOUS():
	def __init__(self,): 
		self.name = "MERETRICIOUS"
		self.definitions = [u'seeming attractive but really false or of little value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
