

#calss header
class _DISTRESSING():
	def __init__(self,): 
		self.name = "DISTRESSING"
		self.definitions = [u'upsetting or worrying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
