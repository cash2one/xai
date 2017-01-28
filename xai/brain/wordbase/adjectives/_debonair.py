

#calss header
class _DEBONAIR():
	def __init__(self,): 
		self.name = "DEBONAIR"
		self.definitions = [u'(especially of men) attractive, confident, and carefully dressed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
