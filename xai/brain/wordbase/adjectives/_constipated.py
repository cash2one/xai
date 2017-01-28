

#calss header
class _CONSTIPATED():
	def __init__(self,): 
		self.name = "CONSTIPATED"
		self.definitions = [u'unable to empty your bowels as often as you should: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
