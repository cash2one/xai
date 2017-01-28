

#calss header
class _DISCORDANT():
	def __init__(self,): 
		self.name = "DISCORDANT"
		self.definitions = [u'producing an unpleasant sound', u'to look or sound different or wrong compared with everything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
