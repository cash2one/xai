

#calss header
class _AV():
	def __init__(self,): 
		self.name = "AV"
		self.definitions = [u'abbreviation for  audiovisual : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
