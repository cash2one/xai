

#calss header
class _TAWDRY():
	def __init__(self,): 
		self.name = "TAWDRY"
		self.definitions = [u'looking bright and attractive but in fact cheap and of low quality']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
