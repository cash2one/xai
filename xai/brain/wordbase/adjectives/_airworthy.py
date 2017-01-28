

#calss header
class _AIRWORTHY():
	def __init__(self,): 
		self.name = "AIRWORTHY"
		self.definitions = [u'An airworthy aircraft is one that is in safe working condition and safe to fly.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
