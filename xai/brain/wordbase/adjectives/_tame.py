

#calss header
class _TAME():
	def __init__(self,): 
		self.name = "TAME"
		self.definitions = [u'(especially of animals) not wild or dangerous, either naturally or because of training or long involvement with humans: ', u'not interesting or exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
