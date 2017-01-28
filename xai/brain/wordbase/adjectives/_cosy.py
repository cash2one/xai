

#calss header
class _COSY():
	def __init__(self,): 
		self.name = "COSY"
		self.definitions = [u'comfortable and pleasant, especially (of a building) because of being small and warm: ', u'used to describe a situation that is convenient for those involved but may not be honest or legal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
