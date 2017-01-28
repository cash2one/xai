

#calss header
class _RAMSHACKLE():
	def __init__(self,): 
		self.name = "RAMSHACKLE"
		self.definitions = [u'badly or untidily made and likely to break or fall down easily: ', u'badly organized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
