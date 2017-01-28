

#calss header
class _WRAPPED():
	def __init__(self,): 
		self.name = "WRAPPED"
		self.definitions = [u'covered with paper or other material: ', u'extremely happy or excited']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
