

#calss header
class _UNSKILLED():
	def __init__(self,): 
		self.name = "UNSKILLED"
		self.definitions = [u'Unskilled people have no particular work skills, and unskilled work does not need any particular skills: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
