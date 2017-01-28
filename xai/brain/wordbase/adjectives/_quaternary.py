

#calss header
class _QUATERNARY():
	def __init__(self,): 
		self.name = "QUATERNARY"
		self.definitions = [u'from or referring to the period of time from about 2.5 million years ago to the present, in which modern humans appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
