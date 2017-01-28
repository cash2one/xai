

#calss header
class _ASIAN():
	def __init__(self,): 
		self.name = "ASIAN"
		self.definitions = [u'belonging to or relating to Asia or its people', u'in the US, Canada, Australia, and New Zealand, belonging to or relating to China, Japan, or countries near them', u'in the UK, belonging to or relating to India, Pakistan, or countries near them']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
