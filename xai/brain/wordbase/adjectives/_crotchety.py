

#calss header
class _CROTCHETY():
	def __init__(self,): 
		self.name = "CROTCHETY"
		self.definitions = [u'often in a bad mood and easily annoyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
