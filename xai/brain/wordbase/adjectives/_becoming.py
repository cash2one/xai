

#calss header
class _BECOMING():
	def __init__(self,): 
		self.name = "BECOMING"
		self.definitions = [u'used to say that something is attractive and suits the person wearing or doing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
