

#calss header
class _GRUESOME():
	def __init__(self,): 
		self.name = "GRUESOME"
		self.definitions = [u'extremely unpleasant and shocking, and usually dealing with death or injury: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
