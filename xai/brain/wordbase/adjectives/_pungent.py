

#calss header
class _PUNGENT():
	def __init__(self,): 
		self.name = "PUNGENT"
		self.definitions = [u'A pungent smell or taste is very strong, sometimes unpleasantly strong: ', u'Pungent speech or writing is very strongly felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
