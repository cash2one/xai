

#calss header
class _FITFUL():
	def __init__(self,): 
		self.name = "FITFUL"
		self.definitions = [u'often stopping and starting and not happening in a regular or continuous way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
