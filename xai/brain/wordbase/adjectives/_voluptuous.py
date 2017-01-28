

#calss header
class _VOLUPTUOUS():
	def __init__(self,): 
		self.name = "VOLUPTUOUS"
		self.definitions = [u'A voluptuous woman has a soft, curved, sexually attractive body: ', u'A voluptuous experience or object gives you a lot of pleasure because it feels extremely soft and comfortable or it sounds or looks extremely beautiful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
