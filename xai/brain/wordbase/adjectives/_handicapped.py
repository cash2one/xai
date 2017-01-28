

#calss header
class _HANDICAPPED():
	def __init__(self,): 
		self.name = "HANDICAPPED"
		self.definitions = [u'not able to use part of your body or your mind because it has been damaged or does not work normally. This word is now considered offensive by many people, who prefer to say someone is disabled or has a disability: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
