

#calss header
class _UNPROTECTED():
	def __init__(self,): 
		self.name = "UNPROTECTED"
		self.definitions = [u'not protected and therefore able to be harmed or damaged: ', u'sexual activity without a condom']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
