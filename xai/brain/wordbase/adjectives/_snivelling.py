

#calss header
class _SNIVELLING():
	def __init__(self,): 
		self.name = "SNIVELLING"
		self.definitions = [u'used to describe someone you do not like because they are weak and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
