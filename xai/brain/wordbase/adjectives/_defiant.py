

#calss header
class _DEFIANT():
	def __init__(self,): 
		self.name = "DEFIANT"
		self.definitions = [u'proudly refusing to obey authority: ', u'not willing to accept criticism or disapproval: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
