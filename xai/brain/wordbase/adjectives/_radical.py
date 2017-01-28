

#calss header
class _RADICAL():
	def __init__(self,): 
		self.name = "RADICAL"
		self.definitions = [u'believing or expressing the belief that there should be great or extreme social or political change: ', u'relating to the most important parts of something or someone; complete or extreme: ', u'aimed at removing all diseased tissue: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
